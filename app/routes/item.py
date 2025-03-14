from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.extensions import db
from app.models.item import Item
from app.models.wishlist import Wishlist

bp = Blueprint('item', __name__, url_prefix='/items')

@bp.route('/create/<int:wishlist_id>', methods=['GET', 'POST'])
@login_required
def create_item(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if wishlist.user_id != current_user.id:
        flash('Доступ запрещен.', 'danger')
        return redirect(url_for('wishlist.list_wishlists'))
    if request.method == 'POST':
        description = request.form.get('description')
        price = request.form.get('price')
        link = request.form.get('link')
        status = request.form.get('status', 'Хочу')
        
        new_item = Item(
            description=description,
            price=float(price) if price else 0.0,
            link=link,
            status=status,
            wishlist_id=wishlist_id
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Товар добавлен!', 'success')
        return redirect(url_for('wishlist.view_wishlist', wishlist_id=wishlist_id))
    return render_template('create_item.html', wishlist=wishlist)
