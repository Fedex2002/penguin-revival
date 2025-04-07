from sanic import Blueprint, response
from sqlalchemy import func

from dash import env
from dash.data.penguin import Penguin
from dash.routes.manager.login import login_auth

verification = Blueprint('verification', url_prefix='/verify')


@verification.get('/')
@login_auth()
async def verify_page(_):
    return response.redirect('/manager/verify/en')


@verification.get('/<lang>')
@login_auth()
async def verify_page(request, lang):
    template = env.get_template('manager/verify.html')
    data = await Penguin.query.where(func.lower(Penguin.username) == request.ctx.session.get('username')).gino.first()
    if lang == 'de':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_de == False) & (Penguin.rejection_de == False)
        ).gino.all()
    elif lang == 'es':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_es == False) & (Penguin.rejection_es == False)
        ).gino.all()
    elif lang == 'fr':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_fr == False) & (Penguin.rejection_fr == False)
        ).gino.all()
    elif lang == 'pt':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_pt == False) & (Penguin.rejection_pt == False)
        ).gino.all()
    elif lang == 'ru':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_ru == False) & (Penguin.rejection_ru == False)
        ).gino.all()
    else:
        lang = 'en'
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
        ).gino.all()
    unverified_penguins = get_paginated_result(unverified_penguins)
    page = template.render(
        success_message='',
        error_message='',
        unverified_penguins=unverified_penguins,
        penguin=data,
        language=lang
    )
    return response.html(page)


@verification.post('/search')
@login_auth()
async def search_username(request):
    template = env.get_template('manager/verify.html')
    username = request.form.get('username', None)
    language = request.form.get('language', None)
    data = await Penguin.query.where(func.lower(Penguin.username) == request.ctx.session.get('username')).gino.first()
    if not language:
        return response.text('You must provide a valid language.')
    elif not username:
        return response.text('You must provide a valid username.')
    if language == 'en':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    elif language == 'de':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_de == False) & (Penguin.rejection_de == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    elif language == 'es':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_es == False) & (Penguin.rejection_es == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    elif language == 'fr':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_fr == False) & (Penguin.rejection_fr == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    elif language == 'pt':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_pt == False) & (Penguin.rejection_pt == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    elif language == 'ru':
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_ru == False) & (Penguin.rejection_ru == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    else:
        language = 'en'
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
            & (Penguin.username.ilike(f"%{username}%"))
        ).gino.all()
    unverified_penguins = get_paginated_result(unverified_penguins)
    page = template.render(
        success_message=f"Searched usernames similar to {username}.",
        error_message='',
        unverified_penguins=unverified_penguins,
        penguin=data,
        language=language
    )
    return response.html(page)


@verification.post('/approve/<penguin_id>')
@login_auth()
async def approve_request(request, penguin_id):
    template = env.get_template('manager/verify.html')
    language = request.form.get('language', None)
    data = await Penguin.query.where(func.lower(Penguin.username) == request.ctx.session.get('username')).gino.first()
    penguin = await Penguin.query.where(Penguin.id == int(penguin_id)).gino.first()
    if not language:
        return response.text('You must provide a valid language.')
    if not penguin:
        return response.text('You must provide a valid penguin ID.')
    if language == 'en':
        await Penguin.update.values(approval_en=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
        ).gino.all()
    elif language == 'de':
        await Penguin.update.values(approval_de=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_de == False) & (Penguin.rejection_de == False)
        ).gino.all()
    elif language == 'es':
        await Penguin.update.values(approval_es=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_es == False) & (Penguin.rejection_es == False)
        ).gino.all()
    elif language == 'fr':
        await Penguin.update.values(approval_fr=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_fr == False) & (Penguin.rejection_fr == False)
        ).gino.all()
    elif language == 'pt':
        await Penguin.update.values(approval_pt=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_pt == False) & (Penguin.rejection_pt == False)
        ).gino.all()
    elif language == 'ru':
        await Penguin.update.values(approval_ru=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_ru == False) & (Penguin.rejection_ru == False)
        ).gino.all()
    else:
        language = 'en'
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
        ).gino.all()
    unverified_penguins = get_paginated_result(unverified_penguins)
    page = template.render(
        success_message=f"Successfully approved {penguin.username}'s username.",
        error_message='',
        unverified_penguins=unverified_penguins,
        penguin=data,
        language=language
    )
    return response.html(page)


@verification.post('/reject/<penguin_id>')
@login_auth()
async def reject_request(request, penguin_id):
    template = env.get_template('manager/verify.html')
    language = request.form.get('language', None)
    data = await Penguin.query.where(func.lower(Penguin.username) == request.ctx.session.get('username')).gino.first()
    penguin = await Penguin.query.where(Penguin.id == int(penguin_id)).gino.first()
    if not language:
        return response.text('You must provide a valid language.')
    if not penguin:
        return response.text('You must provide a valid penguin ID.')
    if language == 'en':
        await Penguin.update.values(rejection_en=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
        ).gino.all()
    elif language == 'de':
        await Penguin.update.values(rejection_de=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_de == False) & (Penguin.rejection_de == False)
        ).gino.all()
    elif language == 'es':
        await Penguin.update.values(rejection_es=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_es == False) & (Penguin.rejection_es == False)
        ).gino.all()
    elif language == 'fr':
        await Penguin.update.values(rejection_fr=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_fr == False) & (Penguin.rejection_fr == False)
        ).gino.all()
    elif language == 'pt':
        await Penguin.update.values(rejection_pt=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_pt == False) & (Penguin.rejection_pt == False)
        ).gino.all()
    elif language == 'ru':
        await Penguin.update.values(rejection_ru=True).where(Penguin.id == penguin.id).gino.status()
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_ru == False) & (Penguin.rejection_ru == False)
        ).gino.all()
    else:
        language = 'en'
        unverified_penguins = await Penguin.query.where(
            (Penguin.approval_en == False) & (Penguin.rejection_en == False)
        ).gino.all()
    unverified_penguins = get_paginated_result(unverified_penguins)
    page = template.render(
        success_message=f"Successfully rejected {penguin.username}'s username.",
        error_message='',
        unverified_penguins=unverified_penguins,
        penguin=data,
        language=language
    )
    return response.html(page)


def get_paginated_result(results):
    paginated_results = {}
    current_count = 0
    pagination_limit = current_count + 10
    page = 1
    for result in results:
        if current_count == 0:
            paginated_results[page] = []
            paginated_results[page].append(result)
        elif current_count == pagination_limit:
            page += 1
            pagination_limit = current_count + 10
            paginated_results[page] = []
            paginated_results[page].append(result)
        else:
            paginated_results[page].append(result)
        current_count += 1
    return paginated_results

