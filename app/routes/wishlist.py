from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.extensions import db
from app.models.wishlist import Wishlist

bp = Blueprint('wishlist', __name__, url_prefix='/wishlists')

@bp.route('/')
@login_required
def list_wishlists():
    wishlists = Wishlist.query.filter_by(user_id=current_user.id).all()
    return render_template('wishlists.html', wishlists=wishlists)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_wishlist():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        is_private = request.form.get('is_private') == 'on'
        
        new_wishlist = Wishlist(title=title, description=description, is_private=is_private, user_id=current_user.id)
        db.session.add(new_wishlist)
        db.session.commit()
        flash('Список желаний создан!', 'success')
        return redirect(url_for('wishlist.list_wishlists'))
    return render_template('create_wishlist.html')

@bp.route('/<int:wishlist_id>')
@login_required
def view_wishlist(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if wishlist.user_id != current_user.id:
        flash('Доступ запрещен.', 'danger')
        return redirect(url_for('wishlist.list_wishlists'))
    return render_template('wishlist.html', wishlist=wishlist)
