from flask import Blueprint, render_template, session
from model.menu_model import MenuModel

index_route = Blueprint('index_route', __name__)

@index_route.route("/")
def index():
    # user_data = session.get('user')
    # if user_data:
    #     user = UserModel(**user_data)
    
    menu = [
        MenuModel(**{"link": "/dashboard", "name":"Dashboard", "icon":"fa fa-dashboard","parent":""}),
        MenuModel(**{"link": "/dashboard/stats", "name":"Thống kê", "icon":"fa fa-chart-bar", "parent":"Dashboard"}),
        MenuModel(**{"link": "/dashboard/reports", "name":"Báo cáo", "icon":"fa fa-file", "parent":"Dashboard"}),
        
        MenuModel(**{"link": "/users", "name":"Quản lý người dùng", "icon":"fa fa-users", "parent":""}),
        MenuModel(**{"link": "/users/list", "name":"Danh sách", "icon":"fa fa-list", "parent":"Quản lý người dùng"}),
        MenuModel(**{"link": "/users/add", "name":"Thêm mới", "icon":"fa fa-plus", "parent":"Quản lý người dùng"}),
        
        MenuModel(**{"link": "/settings", "name":"Cài đặt", "icon":"fa fa-cog", "parent":""}),
        MenuModel(**{"link": "/settings/profile", "name":"Hồ sơ", "icon":"fa fa-user", "parent":"Cài đặt"}),
        MenuModel(**{"link": "/settings/security", "name":"Bảo mật", "icon":"fa fa-lock", "parent":"Cài đặt"}),
        
        # Menu con cấp 3
        MenuModel(**{"link": "/settings/profile/personal", "name":"Thông tin cá nhân", "icon":"fa fa-id-card", "parent":"Hồ sơ"}),
    ]
    
    return render_template("base.html", menu=menu)