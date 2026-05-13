import reflex as rx

config = rx.Config(
    app_name="Desarrollo_Web_con_Reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)