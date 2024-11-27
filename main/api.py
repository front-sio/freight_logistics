from ninja import Router
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from ninja.errors import HttpError
from django.contrib.auth import get_user_model
from django.db import transaction
from .models import AWB, Cost
from .schemas import (
    AWBSchema, 
    CostSchema, 
    LoginSchema, 
    AWBCreateSchema, 
    CostUpdateSchema,
    SignUpSchema,
    TokenResponse,
    AWBSummarySchema, 
    CostSummarySchema, 
    ProfitLossSchema,
    AWBDetailsSchema,
)

# Default Costs
DEFAULT_COSTS = [
    "tbs", "tsc", "tax", "misc_ftr", "misc_ftb", "misc_fto", "other_misc",
    "misc_ogd", "misc1", "misc2", "misc3", "parking", "domestic_tr", "fuel",
    "pcs", "wt_kg", "rate"
]

User = get_user_model()

# Auth Router
auth_router = Router()

@auth_router.post("/token", response=TokenResponse)
def login(request, payload: LoginSchema):
    user = User.objects.filter(username=payload.username).first()
    if not user or not user.check_password(payload.password):
        raise HttpError(401, "Invalid username or password")  

    refresh = RefreshToken.for_user(user)
    return TokenResponse(
        access=str(refresh.access_token),
        refresh=str(refresh),
        user={
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    )

@auth_router.post("/sign-up")
def sign_up(request, payload: SignUpSchema):
    if User.objects.filter(username=payload.username).exists():
        raise HttpError(400, "Username already exists")

    user = User.objects.create_user(
        username=payload.username,
        password=payload.password,
        email=payload.email,
    )

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }

@auth_router.post("/refresh")
def refresh_token(request, refresh: str):
    try:
        refresh_obj = RefreshToken(refresh)
        return {"access": str(refresh_obj.access_token)}
    except Exception:
        raise HttpError(401, "Invalid refresh token")


# Protected Router
protected_router = Router()

@protected_router.post("/awbs", response=AWBSchema)
def create_awb_with_default_costs(request, payload: AWBCreateSchema):
    with transaction.atomic():
        awb = AWB.objects.create(awb_number=payload.awb_number)
        for cost_name in DEFAULT_COSTS:
            Cost.objects.create(
                awb=awb,
                name=cost_name,
                amount=0.00,
                remarks="",
            )
    return AWBSchema.from_orm(awb)


@protected_router.get("/awbs", response=list[AWBSchema])
def awb_list(request):
    return [AWBSchema.from_orm(awb) for awb in AWB.objects.all()]



@protected_router.get("/awbs/{awb_id}/costs", response=list[CostSchema])
def list_awb_costs(request, awb_id: int):
    costs = Cost.objects.filter(awb_id=awb_id)
    return costs  



@protected_router.put("/costs/{cost_id}", response=CostSchema)
def update_cost(request, cost_id: int, payload: CostUpdateSchema):
    try:
        cost = Cost.objects.get(id=cost_id)
    except Cost.DoesNotExist:
        raise HttpError(404, "Cost not found")

    cost.amount = payload.amount
    cost.remarks = payload.remarks
    cost.save()
    return cost  


@protected_router.get("/awb-list", response=list[AWBSchema])
def awb_list(request):
    return [AWBSchema.from_orm(awb) for awb in AWB.objects.all()]


@protected_router.get("/awb-summary", response=AWBSummarySchema)
def get_awb_summary(request):
    total_awbs = AWB.objects.count()
    return {"total": total_awbs, "delivered": 0, "pending": total_awbs}

@protected_router.get("/cost-summary", response=CostSummarySchema)
def get_cost_summary(request):
    total_costs = Cost.objects.aggregate(total=models.Sum("amount"))["total"] or 0
    return {"totalCosts": total_costs, "completed": 0, "pending": 0}

@protected_router.get("/profit-loss", response=ProfitLossSchema)
def get_profit_loss(request):
    total_revenue = sum(awb.calculate_revenue() for awb in AWB.objects.all())
    total_cost = sum(cost.amount for cost in Cost.objects.all())
    profit = max(0, total_revenue - total_cost)
    loss = max(0, total_cost - total_revenue)
    return {
        "revenue": total_revenue,
        "total_cost": total_cost,
        "profit": profit,
        "loss": loss,
    }
