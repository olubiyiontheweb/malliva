from fastapi.encoders import jsonable_encoder
from services.authentication import authenticate
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from schema.categories import Category
from models.categories import Category as CategoryModel
from config.config_loader import settings
from services.python_operations import convert_mongo_result_to_dict, loop_through_queryset
from dbConnectionManager.db_session import accounts_db_connection_instance

router = APIRouter()
