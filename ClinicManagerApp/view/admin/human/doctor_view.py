import cloudinary.uploader
from flask_admin.contrib.sqla.filters import FilterEqual, FilterNotEqual, FilterLike, FilterNotLike, DateEqualFilter, \
    DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, DateBetweenFilter, BooleanEqualFilter, \
    BooleanNotEqualFilter, FloatEqualFilter, FloatNotEqualFilter, FloatGreaterFilter, FloatSmallerFilter
from flask_admin.form import rules
from wtforms import validators, EmailField, DateField, TelField, FileField

from ClinicManagerApp.model.human.doctor_model import DoctorModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class DoctorView(BaseModelView):
    # columns
    column_sortable_list = ['staff_id',
                            'first_name',
                            'last_name',
                            'date_of_birth',
                            'date_of_work',
                            'exp_year',
                            'id_card']
    column_searchable_list = ['staff_id']
    column_filters = (FilterEqual(DoctorModel.first_name, name='Tên'),
                      FilterNotEqual(DoctorModel.first_name, name='Tên'),
                      FilterLike(DoctorModel.first_name, name='Tên'),
                      FilterNotLike(DoctorModel.first_name, name='Tên'),
                      FilterEqual(DoctorModel.last_name, name='Họ và tên đệm'),
                      FilterNotEqual(DoctorModel.last_name, name='Họ và tên đệm'),
                      FilterLike(DoctorModel.last_name, name='Họ và tên đệm'),
                      FilterNotLike(DoctorModel.last_name, name='Họ và tên đệm'),
                      DateEqualFilter(DoctorModel.date_of_birth, name='Ngày sinh'),
                      DateNotEqualFilter(DoctorModel.date_of_birth, name='Ngày sinh'),
                      DateGreaterFilter(DoctorModel.date_of_birth, name='Ngày sinh'),
                      DateSmallerFilter(DoctorModel.date_of_birth, name='Ngày sinh'),
                      DateBetweenFilter(DoctorModel.date_of_birth, name='Ngày sinh'),
                      FilterEqual(DoctorModel.sex, name='Giới tính'),
                      FilterNotEqual(DoctorModel.sex, name='Giới tính'),
                      FilterLike(DoctorModel.sex, name='Giới tính'),
                      FilterNotLike(DoctorModel.sex, name='Giới tính'),
                      FilterEqual(DoctorModel.id_card, name='Căn cước công dân'),
                      FilterNotEqual(DoctorModel.id_card, name='Căn cước công dân'),
                      FilterLike(DoctorModel.id_card, name='Căn cước công dân'),
                      FilterNotLike(DoctorModel.id_card, name='Căn cước công dân'),
                      FilterLike(DoctorModel.address, name='Địa chỉ'),
                      FilterNotLike(DoctorModel.address, name='Địa chỉ'),
                      FilterLike(DoctorModel.email, name='Email'),
                      FilterNotLike(DoctorModel.email, name='Email'),
                      FilterEqual(DoctorModel.phone_number, name='Số điện thoại'),
                      DateEqualFilter(DoctorModel.date_of_work, name='Ngày vào làm'),
                      DateNotEqualFilter(DoctorModel.date_of_work, name='Ngày vào làm'),
                      DateGreaterFilter(DoctorModel.date_of_work, name='Ngày vào làm'),
                      DateSmallerFilter(DoctorModel.date_of_work, name='Ngày vào làm'),
                      DateBetweenFilter(DoctorModel.date_of_work, name='Ngày vào làm'),
                      FloatEqualFilter(DoctorModel.exp_year, name='Kinh nghiệm (năm)'),
                      FloatNotEqualFilter(DoctorModel.exp_year, name='Kinh nghiệm (năm)'),
                      FloatGreaterFilter(DoctorModel.exp_year, name='Kinh nghiệm (năm)'),
                      FloatSmallerFilter(DoctorModel.exp_year, name='Kinh nghiệm (năm)'))

    column_default_sort = 'staff_id'

    column_labels = dict(staff_id='Mã',
                         first_name='Tên',
                         last_name='Họ và tên đệm',
                         date_of_birth='Ngày sinh',
                         sex='Giới tính',
                         address='Địa chỉ',
                         email='Email',
                         phone_number='Số điện thoại',
                         date_of_work='Ngày vào làm',
                         major='Chuyên ngành',
                         exp_year='Kinh nghiệm (năm)',
                         manager='Người quản lý',
                         contained_department='Khoa trực thuộc',
                         managed_department='Khoa quản lý',
                         staff_list='Danh sách nhân viên quản lý',
                         account='Tài khoản',
                         id_card='Căn cước công dân',
                         avatar='Ảnh đại diện',
                         facebook_link= 'Facebook',
                         twitter_link='Twitter'
                         )
    column_list = ('staff_id',
                   'first_name',
                   'last_name',
                   'date_of_birth',
                   'sex',
                   'id_card',
                   'address',
                   'email',
                   'phone_number',
                   'date_of_work',
                   'major',
                   'exp_year',
                   'avatar',
                   'manager',
                   'contained_department',
                   'account',
                   'facebook_link',
                   'twitter_link'
                   )

    # form
    form_rules = [
        # Define field set with header text and four fields
        rules.FieldSet(('first_name',
                        'last_name',
                        'date_of_birth',
                        'sex',
                        'id_card',
                        'address',
                        'email',
                        'phone_number',
                        'date_of_work',
                        'major',
                        'exp_year',
                        'avatar',
                        'facebook_link',
                        'twitter_link'), 'Thông tin bác sĩ'),

        rules.FieldSet(('manager',
                        'contained_department',
                        'managed_department',
                        'staff_list',
                        'account'), 'Thông tin khác có liên quan'),

    ]
    form_extra_fields = {
        'email': EmailField('Email',
                            validators=[validators.Length(min=0, max=50)],
                            render_kw={
                                'placeholder': 'Địa chỉ email bác sĩ'
                            }),
        'date_of_birth': DateField('Ngày sinh', validators=[validators.DataRequired()]),
        'date_of_work': DateField('Ngày vào làm', validators=[validators.DataRequired()]),
        'phone_number': TelField('Số điện thoại',
                                 validators=[validators.Length(min=9, max=10)],
                                 render_kw={
                                     'placeholder': 'Số điện thoại bác sĩ'
                                 }),
        'avatar': FileField('Ảnh đại diện')
    }
    form_args = dict(
        first_name=dict(validators=[validators.DataRequired(),
                                    validators.Length(min=1, max=20)],
                        render_kw={
                            'placeholder': 'Tên bác sĩ'
                        }),
        last_name=dict(validators=[validators.DataRequired(),
                                   validators.Length(min=1, max=50)],
                       render_kw={
                           'placeholder': 'Họ và tên đệm bác sĩ'
                       }),
        address=dict(validators=[validators.DataRequired(),
                                 validators.Length(min=1, max=150)],
                     render_kw={
                         'placeholder': 'Địa chỉ bác sĩ'
                     }),
        exp_year=dict(validators=[validators.NumberRange(min=0.0, max=50.0)], ),

        id_card=dict(validators=[validators.Length(min=10, max=12), validators.DataRequired()],
                     render_kw={
                         'placeholder': 'Căn cước công dân bác sĩ'
                     })
    )

    def on_model_change(self, form, staff_model, is_created):
        if form.avatar.data:
            res = cloudinary.uploader.upload(form.avatar.data, folder='avatar_staff')
            staff_model.set_avatar(str(res['secure_url']))
        else:
            staff_model.set_avatar('')

    def scaffold_list_columns(self):
        return ['staff_id',
                'first_name',
                'last_name',
                'date_of_birth',
                'sex',
                'id_card',
                'address',
                'email',
                'phone_number',
                'date_of_work',
                'major',
                'exp_year',
                'avatar',
                'manager',
                'contained_department',
                'managed_department',
                'staff_list',
                'account',
                'facebook_link',
                'twitter_link'
                ]
