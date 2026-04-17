from layouts.title import create_title
from layouts.dropdowns_menu import create_dropdowns_menu
from layouts.dashboard import create_dashboard
from layouts.footer import create_footer
from callbacks.callbacks import register_callbacks

from app import app

register_callbacks()

app.layout = [
    create_title(),
    create_dropdowns_menu(),
    create_dashboard(),
    create_footer()
]

if __name__ == '__main__':
    app.run(debug=True)