import os
from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

from .controllers import controllers
from ...infrastructure.db.db import alchemy

app = Litestar(
    route_handlers=[controllers],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
    plugins=[alchemy]
)