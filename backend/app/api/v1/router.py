from fastapi import APIRouter

from backend.app.api.v1.address.address_db import router as address_db_router
from backend.app.api.v1.address.address_match_review import router as address_match_review_router
from backend.app.api.v1.address.address_parse import router as address_parse_router
from backend.app.api.v1.admin.admin_api_keys import router as admin_api_keys_router
from backend.app.api.v1.admin.admin_users import router as admin_users_router
from backend.app.api.v1.admin.boundary_admin import router as boundary_admin_router
from backend.app.api.v1.admin.lookup_admin import router as lookup_admin_router
from backend.app.api.v1.auth.auth import router as auth_router
from backend.app.api.v1.ingest.ingest import router as ingest_router
from backend.app.api.v1.ops.ops import router as ops_router
from backend.app.api.v1.search.search import router as search_router


api_router = APIRouter()
api_router.include_router(ops_router)
api_router.include_router(auth_router)
api_router.include_router(search_router)
api_router.include_router(address_db_router)
api_router.include_router(address_parse_router)
api_router.include_router(ingest_router)
api_router.include_router(admin_api_keys_router)
api_router.include_router(admin_users_router)
api_router.include_router(address_match_review_router)
api_router.include_router(boundary_admin_router)
api_router.include_router(lookup_admin_router)
