# Django Online Marketplace

A modern, full-featured online marketplace built with Django that allows users to buy and sell items with an integrated messaging system for seamless communication between buyers and sellers.

## 🌟 Features

- **User Authentication**: Complete user registration, login, and logout functionality
- **Item Management**: Users can create, edit, delete, and browse items
- **Advanced Search**: Search items by name, description, and category
- **Category System**: Organized item categorization for better browsing experience
- **Multiple Image Support**: Upload and manage multiple images per item
- **Messaging**: Integrated conversation system between buyers and sellers
- **User Dashboard**: Personal dashboard to manage your listed items
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS styling
- **Item Conditions**: Support for different item conditions (New, Used - Like New, etc.)
- **Location-based Listings**: Items include location information for local trading

## 🛠 Technologies Used

### Backend
- **Django 5.2.4** - Python web framework
- **SQLite** - Database (easily configurable to PostgreSQL/MySQL)
- **Pillow 11.3.0** - Image processing library
- **Python 3.x** - Programming language

### Frontend
- **HTML5** - Markup language
- **Tailwind CSS** - Utility-first CSS framework
- **Django Templates** - Server-side templating

### Development Tools
- **python-dotenv** - Environment variable management
- **Django Admin** - Built-in admin interface

## 📁 Project Structure

```
marketplace/
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── db.sqlite3                 # SQLite database
├── README.md                  # Project documentation
├── media/                     # User-uploaded files
│   └── item_images/          # Item images storage
├── marketplace/               # Main project configuration
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── core/                      # Core app (homepage, auth)
│   ├── models.py
│   ├── views.py             # Homepage and authentication views
│   ├── forms.py             # Login and signup forms
│   ├── urls.py
│   ├── static/core/         # Core app static files
│   ├── templates/core/      # Core app templates
│   │   ├── base.html        # Base template
│   │   ├── index.html       # Homepage
│   │   ├── login.html       # Login page
│   │   ├── signup.html      # Registration page
│   │   └── contact.html     # Contact page
│   └── migrations/
├── item/                      # Item management app
│   ├── models.py            # Item and Category models
│   ├── views.py             # Item CRUD operations
│   ├── forms.py             # Item creation/editing forms
│   ├── urls.py
│   ├── admin.py
│   ├── static/item/         # Item app static files
│   ├── templates/item/      # Item app templates
│   │   ├── detail.html      # Item detail page
│   │   ├── form.html        # Item creation/editing form
│   │   └── search.html      # Search results page
│   └── migrations/
├── conversation/              # Messaging system app
│   ├── models.py            # Conversation and Message models
│   ├── views.py             # Conversation management
│   ├── forms.py             # Message forms
│   ├── urls.py
│   ├── templates/conversation/
│   └── migrations/
├── dashboard/                 # User dashboard app
│   ├── models.py
│   ├── views.py             # User's items dashboard
│   ├── urls.py
│   ├── templates/dashboard/
│   └── migrations/
└── explaination/             # Development documentation
    ├── conversation.md
    ├── model_images.md
    ├── validation.md
    └── [other documentation files]
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abdelrahman-Yasser-Zakaria/Online-Marketplace.git
   cd Online-Marketplace/marketplace
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv marketplace_env
   
   # On Windows
   marketplace_env\Scripts\activate
   
   # On macOS/Linux
   source marketplace_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your web browser and navigate to `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

## 📝 Usage Guide

### For Users

1. **Registration**: Create a new account using the signup form
2. **Browse Items**: View available items on the homepage
3. **Search**: Use the search functionality to find specific items
4. **Item Details**: Click on any item to view detailed information
5. **Contact Seller**: Start a conversation with item owners
6. **Dashboard**: Manage your listed items from your personal dashboard

### For Sellers

1. **List Items**: Add new items for sale with multiple images
2. **Manage Listings**: Edit or delete your items from the dashboard
3. **Respond to Inquiries**: Communicate with potential buyers through the messaging system
4. **Track Sales**: Mark items as sold when transactions are complete

## 🔧 Configuration

### Database Configuration

The project uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` setting in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'marketplace_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Deployment

### Production Settings

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static files serving
5. Set up media files storage (AWS S3, Cloudinary, etc.)

### Static Files

```bash
python manage.py collectstatic
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 👨‍💻 Author

**Abdelrahman Yasser Zakaria**
- GitHub: [@Abdelrahman-Yasser-Zakaria](https://github.com/Abdelrahman-Yasser-Zakaria)

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information

---

**Note**: This project is designed for educational purposes and may require additional security considerations for production use.
