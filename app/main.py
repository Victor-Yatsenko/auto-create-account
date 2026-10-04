# from fastapi import FastAPI, Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi_babel import BabelMiddleware, _
# from pathlib import Path
# import uvicorn

# from app.core.i18n import babel_configs

# app = FastAPI()

# # 1. Задаем точные абсолютные пути
# BASE_DIR = Path(__file__).resolve().parent.parent
# APP_DIR = BASE_DIR / "app"                      

# # 2. Инициализируем шаблоны и статику
# templates = Jinja2Templates(directory=str(APP_DIR / "templates"))
# app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")


# app.add_middleware(BabelMiddleware, babel_configs=babel_configs, jinja2_templates=templates)


# @app.get("/")
# async def read_root(request: Request):
#     context = {
#         "title": "Auto create account",
#         "message": _("HI")
#     }
    
#     a = _("Text")

#     return templates.TemplateResponse(
#         request=request, 
#         name="index.html", 
#         context=context
#     )


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)



# # # class UserProviderFactory:
# # #     @staticmethod
# # #     def get_provider(infrastructure_type: str):
# # #         if infrastructure_type == "HYBRID_AD":
# # #             return LDAPUserProvider()
# # #         elif infrastructure_type == "ENTRA_CLOUD":
# # #             return EntraIDUserProvider()
# # #         elif infrastructure_type == "GOOGLE_WORKSPACE":
# # #             return GoogleWorkspaceProvider()
# # #         else:
# # #             raise ValueError("Unknown infrastructure type")
