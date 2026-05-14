import reflex as rx


class State(rx.State):
    pass

PINK_DARK  = "#c9848a"
PINK_MED   = "#e8a0a6"
PINK_LIGHT = "#f2d4d6"
PINK_BG    = "#f9eded"
WHITE      = "#ffffff"
BLACK      = "#1a1a1a"
GRAY_TEXT  = "#888"

def top_bar():
    return rx.box(
        rx.hstack(
            rx.text(
                "Same Day Guaranteed Fastest Delivery",
                font_size="0.75rem",
                color="white",
                font_weight="500",
            ),
            rx.hstack(
                rx.text("📞 80001234567", font_size="0.75rem", color="white"),
                rx.text("✉ info@beautyshop.com", font_size="0.75rem", color="white"),
                spacing="5",
            ),
            justify="between",
            width="100%",
            align="center",
        ),
        background=PINK_DARK,
        padding="7px 48px",
    )

def navbar():
    return rx.box(
        rx.hstack(
            # Logo
            rx.vstack(
                rx.text(
                    "BEAUTY·",
                    font_size="1.6rem",
                    font_weight="900",
                    color=BLACK,
                    letter_spacing="-0.02em",
                    line_height="1",
                ),
                rx.text(
                    "BODY ANGELS",
                    font_size="0.55rem",
                    font_weight="600",
                    color=GRAY_TEXT,
                    letter_spacing="0.18em",
                ),
                spacing="0",
                align="start",
            ),
            # Nav links
            rx.hstack(
                rx.box(
                    rx.link(
                        "SHOP ALL",
                        href="#featured",
                        color=BLACK,
                        font_size="0.82rem",
                        font_weight="600",
                        text_decoration="none",
                        _hover={"color": PINK_DARK},
                    ),
                    border_bottom=f"2px solid {PINK_DARK}",
                    padding_bottom="2px",
                ),
                rx.link("Skin Care",  href="#featured", color=BLACK, font_size="0.82rem", font_weight="500", text_decoration="none", _hover={"color": PINK_DARK}),
                rx.link("Solutions",  href="#sale",     color=BLACK, font_size="0.82rem", font_weight="500", text_decoration="none", _hover={"color": PINK_DARK}),
                rx.link("Wishlist",   href="#blog",     color=BLACK, font_size="0.82rem", font_weight="500", text_decoration="none", _hover={"color": PINK_DARK}),
                spacing="7",
                display=["none", "none", "none", "flex"],
                align="center",
            ),
            # Right
            rx.hstack(
                rx.html(
                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#333"'
                    ' stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
                    '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>'
                    '<circle cx="12" cy="7" r="4"/>'
                    '</svg>'
                ),
                rx.html(
                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#333"'
                    ' stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
                    '<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/>'
                    '<line x1="3" y1="6" x2="21" y2="6"/>'
                    '<path d="M16 10a4 4 0 0 1-8 0"/>'
                    '</svg>'
                ),
                rx.link(
                    rx.box(
                        rx.text("SHOP NOW", font_size="0.78rem", font_weight="700", color="white"),
                        background=PINK_DARK,
                        border_radius="999px",
                        padding="9px 22px",
                        cursor="pointer",
                        _hover={"background": "#b57278"},
                    ),
                    href="#featured",
                    text_decoration="none",
                ),
                spacing="4",
                align="center",
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        background="white",
        border_bottom=f"1px solid {PINK_LIGHT}",
        padding="14px 48px",
        position="sticky",
        top="0",
        z_index="1000",
        display="flex",
        align_items="center",
    )

def hero():
    return rx.box(
        # Imagen de fondo
        rx.image(
            src="/hero_bg.jpg",
            width="100%",
            height="100%",
            object_fit="cover",
            position="absolute",
            top="0",
            left="0",
            z_index="0",
        ),
        rx.box(
            background="rgba(180, 110, 115, 0.35)",
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            z_index="1",
        ),
        # Contenido
        rx.vstack(
            rx.text(
                "✦ ✦ ✦",
                font_size="0.8rem",
                color="rgba(255,255,255,0.85)",
                letter_spacing="0.3em",
            ),
            rx.heading(
                "Glow like\nnever before!",
                font_size=["2rem", "2.8rem", "3.4rem"],
                font_weight="800",
                color="white",
                text_align="center",
                line_height="1.15",
                letter_spacing="-0.01em",
                white_space="pre-line",
            ),
            rx.link(
                rx.box(
                    rx.text("SHOP NOW", font_size="0.85rem", font_weight="700", color="white"),
                    background=PINK_DARK,
                    border_radius="999px",
                    padding="12px 36px",
                    cursor="pointer",
                    _hover={"background": "#b57278"},
                    box_shadow="0 4px 16px rgba(180,100,110,0.4)",
                ),
                href="#featured",
                text_decoration="none",
            ),
            spacing="5",
            align="center",
            position="relative",
            z_index="2",
        ),
        id="hero",
        position="relative",
        height=["340px", "420px", "480px"],
        overflow="hidden",
        display="flex",
        align_items="center",
        justify_content="center",
    )

def product_card(name: str, category: str, price: str, image: str, bg: str):
    return rx.box(
        rx.vstack(
            # Imagen del producto
            rx.box(
                rx.image(
                    src=f"/{image}",
                    width="100%",
                    height="160px",
                    object_fit="cover",
                    border_radius="8px",
                ),
                width="100%",
                border_radius="8px",
                overflow="hidden",
                background=bg,
            ),
            # Info
            rx.vstack(
                rx.text(name,     font_weight="700", font_size="0.85rem", color=BLACK),
                rx.text(category, font_size="0.72rem", color=GRAY_TEXT),
                rx.text(price,    font_size="0.82rem", color=PINK_DARK, font_weight="700"),
                rx.hstack(
                    rx.text("★★★★☆", font_size="0.72rem", color=PINK_DARK),
                    rx.text(
                        "Shop Now →",
                        font_size="0.72rem",
                        color=PINK_DARK,
                        font_weight="600",
                        cursor="pointer",
                        _hover={"text_decoration": "underline"},
                    ),
                    justify="between",
                    width="100%",
                ),
                spacing="1",
                align="start",
                width="100%",
                padding="10px 2px 2px",
            ),
            spacing="0",
            width="100%",
        ),
        background="white",
        border_radius="10px",
        padding="10px",
        box_shadow="0 2px 12px rgba(0,0,0,0.06)",
        border=f"1px solid {PINK_LIGHT}",
        flex="1",
        min_width="150px",
        max_width="195px",
        cursor="pointer",
        _hover={
            "box_shadow": "0 8px 28px rgba(180,100,110,0.18)",
            "transform": "translateY(-4px)",
            "transition": "all 0.22s",
        },
    )


def featured_products():
    products = [
        ("Lip Shades",   "LIPSTICKS",  "$24.99", "producto1.png", "#f5e6e8"),
        ("Foundation",   "FOUNDATION", "$38.00", "producto2.png", "#fde8d8"),
        ("Bronzer Glow", "BRONZER",    "$29.50", "producto3.png", "#f5dcc8"),
        ("Powder Blush", "BLUSH",      "$32.00", "producto4.png", "#f9e8e8"),
        ("Skin Radiant", "SKINCARE",   "$45.00", "producto5.png", "#fce8ec"),
    ]
    return rx.box(
        rx.vstack(
            rx.heading(
                "Featured Product",
                font_size="1.5rem",
                font_weight="800",
                color=BLACK,
                text_align="center",
                letter_spacing="-0.01em",
            ),
            rx.flex(
                *[
                    product_card(name, cat, price, img, bg)
                    for name, cat, price, img, bg in products
                ],
                flex_wrap="wrap",
                gap="5",
                justify="center",
                width="100%",
                margin_top="20px",
            ),
            spacing="4",
            align="center",
        ),
        id="featured",
        padding="56px 48px",
        background="white",
    )

def sale_banner():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(
                    "Spring Beauty Sale",
                    font_size=["1.8rem", "2.2rem"],
                    font_weight="900",
                    color=BLACK,
                    letter_spacing="-0.02em",
                    line_height="1.1",
                ),
                rx.heading(
                    "Up to 40% Off",
                    font_size=["1.8rem", "2.2rem"],
                    font_weight="900",
                    color=BLACK,
                    letter_spacing="-0.02em",
                    line_height="1.1",
                ),
                rx.text(
                    "Shop our curated collection of premium beauty products "
                    "at unbeatable prices. Limited time offer for spring season.",
                    font_size="0.85rem",
                    color="#666",
                    max_width="380px",
                    line_height="1.6",
                ),
                rx.hstack(
                    rx.text("⭐⭐⭐⭐⭐", font_size="0.8rem"),
                    rx.text("4.9 · 10,000+ reviews", font_size="0.78rem", color=GRAY_TEXT),
                    spacing="2",
                    align="center",
                ),
                rx.hstack(
                    rx.link(
                        rx.box(
                            rx.text("SHOP NOW", font_size="0.82rem", font_weight="700", color="white"),
                            background=PINK_DARK,
                            border_radius="999px",
                            padding="11px 30px",
                            cursor="pointer",
                            _hover={"background": "#b57278"},
                        ),
                        href="#featured",
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.box(
                            rx.text("EXPLORE MORE", font_size="0.82rem", font_weight="700", color=PINK_DARK),
                            border=f"2px solid {PINK_DARK}",
                            border_radius="999px",
                            padding="11px 24px",
                            cursor="pointer",
                            _hover={"background": PINK_LIGHT},
                        ),
                        href="#featured",
                        text_decoration="none",
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                ),
                spacing="4",
                align="start",
                flex="1",
            ),
            rx.box(
                rx.image(
                    src="/sale_bg.jpg",
                    width="100%",
                    height="300px",
                    object_fit="cover",
                    border_radius="16px",
                ),
                flex="1",
                display=["none", "none", "block"],
                min_width="280px",
                max_width="420px",
            ),
            spacing="9",
            align="center",
            width="100%",
            flex_wrap="wrap",
        ),
        id="sale",
        background=PINK_BG,
        padding="64px 48px",
    )

def blog_card(title: str, category: str, desc: str, image: str):
    return rx.box(
        rx.vstack(
            # Imagen
            rx.box(
                rx.image(
                    src=f"/{image}",
                    width="100%",
                    height="190px",
                    object_fit="cover",
                    border_radius="10px",
                ),
                width="100%",
                border_radius="10px",
                overflow="hidden",
            ),
            # Texto
            rx.vstack(
                rx.text(
                    category,
                    font_size="0.7rem",
                    font_weight="700",
                    color=PINK_DARK,
                    letter_spacing="0.1em",
                ),
                rx.text(
                    title,
                    font_weight="700",
                    font_size="1rem",
                    color=BLACK,
                    line_height="1.3",
                ),
                rx.text(
                    desc,
                    font_size="0.82rem",
                    color=GRAY_TEXT,
                    line_height="1.55",
                ),
                rx.hstack(
                    rx.text("glidebeauty.com", font_size="0.75rem", color=PINK_MED),
                    rx.text("· 5 min read",    font_size="0.75rem", color=GRAY_TEXT),
                    spacing="1",
                ),
                spacing="2",
                align="start",
                width="100%",
                padding="14px 4px 4px",
            ),
            spacing="0",
            width="100%",
        ),
        background="white",
        border_radius="12px",
        padding="12px",
        box_shadow="0 2px 14px rgba(0,0,0,0.06)",
        border=f"1px solid {PINK_LIGHT}",
        flex="1",
        min_width="240px",
        max_width="310px",
        cursor="pointer",
        _hover={
            "box_shadow": "0 6px 28px rgba(180,100,110,0.14)",
            "transform": "translateY(-3px)",
            "transition": "all 0.2s",
        },
    )


def blog_section():
    cards = [
        (
            "Nude Cosmetics",
            "SKINCARE",
            "Discover the best nude shades for every skin tone. Natural beauty at its finest.",
            "blog1.jpg",
        ),
        (
            "Winter Collections",
            "MAKEUP",
            "Explore our seasonal collection with warm tones and long-lasting formulas.",
            "blog2.jpg",
        ),
        (
            "Beauty Routines",
            "LIFESTYLE",
            "Build a morning and night beauty routine that works for your skin type.",
            "blog3.jpg",
        ),
    ]
    return rx.box(
        rx.flex(
            *[blog_card(t, c, d, i) for t, c, d, i in cards],
            flex_wrap="wrap",
            gap="5",
            justify="center",
            width="100%",
        ),
        id="blog",
        padding="56px 48px",
        background="white",
    )

def footer():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.html('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c9848a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>'),
                rx.text("Newsletter",              font_weight="700", font_size="0.88rem", color=BLACK),
                rx.text("Subscribe for updates",  font_size="0.75rem", color=GRAY_TEXT),
                spacing="1",
                align="start",
            ),
            rx.vstack(
                rx.html('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c9848a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'),
                rx.text("Location",               font_weight="700", font_size="0.88rem", color=BLACK),
                rx.text("123 Beauty Ave, NY",     font_size="0.75rem", color=GRAY_TEXT),
                spacing="1",
                align="start",
            ),
            rx.vstack(
                rx.html('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c9848a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 8.81 19.79 19.79 0 0 1 1.6 2.18 2 2 0 0 1 3.57 0h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 7.91a16 16 0 0 0 6.13 6.13l.91-.91a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'),
                rx.text("500+ WhatsApp",          font_weight="700", font_size="0.88rem", color=BLACK),
                rx.text("Beauty Group",           font_size="0.75rem", color=GRAY_TEXT),
                spacing="1",
                align="start",
            ),
  
            rx.hstack(
                rx.link(
                    rx.box(
                        rx.text("f", font_size="0.75rem", color="white", font_weight="700"),
                        background="#1a1a1a",
                        border_radius="50%",
                        width="34px",
                        height="34px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        cursor="pointer",
                        _hover={"background": PINK_DARK},
                    ),
                    href="https://www.facebook.com",
                    is_external=True,
                ),
                rx.link(
                    rx.box(
                        rx.text("yt", font_size="0.75rem", color="white", font_weight="700"),
                        background="#1a1a1a",
                        border_radius="50%",
                        width="34px",
                        height="34px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        cursor="pointer",
                        _hover={"background": PINK_DARK},
                    ),
                    href="https://www.youtube.com",
                    is_external=True,
                ),
                rx.link(
                    rx.box(
                        rx.html(
                            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"'
                            ' stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                            '<rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>'
                            '<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>'
                            '<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>'
                            '</svg>'
                        ),
                        background="#1a1a1a",
                        border_radius="50%",
                        width="34px",
                        height="34px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        cursor="pointer",
                        _hover={"background": "#e1306c"},
                    ),
                    href="https://www.instagram.com/loeftones?igsh=bmZiNmgyNnpoMXN0&utm_source=qr",
                    is_external=True,
                ),
                rx.link(
                    rx.box(
                        rx.text("in", font_size="0.75rem", color="white", font_weight="700"),
                        background="#1a1a1a",
                        border_radius="50%",
                        width="34px",
                        height="34px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        cursor="pointer",
                        _hover={"background": PINK_DARK},
                    ),
                    href="https://www.linkedin.com",
                    is_external=True,
                ),
                rx.link(
                    rx.box(
                        rx.text("tw", font_size="0.75rem", color="white", font_weight="700"),
                        background="#1a1a1a",
                        border_radius="50%",
                        width="34px",
                        height="34px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        cursor="pointer",
                        _hover={"background": PINK_DARK},
                    ),
                    href="https://www.twitter.com",
                    is_external=True,
                ),
                spacing="2",
                align="center",
            ),
            justify="between",
            align="center",
            width="100%",
            flex_wrap="wrap",
            gap="5",
        ),
        background=PINK_LIGHT,
        padding="28px 48px",
    )
 
def index():
    return rx.box(
        top_bar(),
        navbar(),
        hero(),
        featured_products(),
        sale_banner(),
        blog_section(),
        footer(),
        style={"scroll_behavior": "smooth"},
        background="white",
        font_family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"
    ],
    style={"font_family": "Inter, sans-serif"},
)
app.add_page(index, route="/", title="Beauty — Body Angels")