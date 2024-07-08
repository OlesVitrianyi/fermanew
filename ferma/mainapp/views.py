from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from mainapp.models import *
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import calendar
import logging
from calendar import HTMLCalendar
from .ukrainian_months import ukrainian_months
from userapp.models import Profile


def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email_message = EmailMessage(
            subject=f"{name}, гість сторінки fermanew.com",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email_message.send()

        messages.success(request, "Повідомлення надіслано успішно!")
        return redirect('index')

    return render(request, 'mainapp/index.html')


def index(request):
    # response = feedback_view(request)
    # if response:
    #     return response
    # response = feedback_view(request)
    response = feedback_view(request)
    advertisement_post = PostClass.objects.filter(cat_id=1, is_published=True)[:1]  # оголошення
    information_post = PostClass.objects.filter(cat_id=2, is_published=True)[:1]
    cats = CategoryClass.objects.all()
    context = {
        'title': 'Головна сторінка Ferma New',
        'advertisement_post': advertisement_post,
        'information_post': information_post,
        'cats': cats,
        'response': response,
    }
    return render(request, 'mainapp/index.html', context=context)


def about_us(request):
    context = {
        'title': 'Про відпочинковий комплекс Ferma New',
    }
    return render(request, 'mainapp/about_us.html', context=context)


def bank_details(request):
    context = {
        'title': 'Реквізити банківського рахунку Ferma New',
    }
    return render(request, 'mainapp/bank_details.html', context=context)


def contact_us(request):
    response = feedback_view(request)
    context = {
        'title': 'Звʼязок із відпочинковим комплексом Ferma New',
        'response': response,
    }
    return render(request, 'mainapp/contact_us.html', context=context)


def rules_of_stay(request):
    context = {
        'title': 'Правила перебування гостей Ferma New',
    }
    return render(request, 'mainapp/documents/rules_of_stay.html', context=context)


def check_in_rules(request):
    context = {
        'title': 'Правила заселення гостей Ferma New',
    }
    return render(request, 'mainapp/documents/check_in_rules.html', context=context)


def booking_rules(request):
    context = {
        'title': 'Правила бронювання будинків Ferma New',
    }
    return render(request, 'mainapp/documents/booking_rules.html', context=context)


def privacy_policy(request):
    context = {
        'title': 'Політика конфіденційності Ferma New',
    }
    return render(request, 'mainapp/documents/privacy_policy.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(PostClass, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'mainapp/post.html', context=context)


def add_months(year, month, num_months):
    new_month = month + num_months
    new_year = year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1
    return new_year, new_month


def get_calendar_data(holidayhouse_id):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    # Отримуємо дані для поточного, наступного і третього місяців
    cal_current_month = calendar.monthcalendar(current_year, current_month)
    next_year, next_month = add_months(current_year, current_month, 1)
    cal_next_month = calendar.monthcalendar(next_year, next_month)
    third_year, third_month = add_months(current_year, current_month, 2)
    cal_third_month = calendar.monthcalendar(third_year, third_month)

    # Фільтруємо booked_dates для поточного місяця
    current_month_booked_dates = BookingHouseClass.objects.filter(
        holidayhouse_id=holidayhouse_id, day__year=current_year, day__month=current_month
    ).values_list('day__day', flat=True)

    # Фільтруємо booked_dates для наступного місяця
    next_month_booked_dates = BookingHouseClass.objects.filter(
        holidayhouse_id=holidayhouse_id, day__year=next_year, day__month=next_month
    ).values_list('day__day', flat=True)

    # Фільтруємо booked_dates для третього місяця
    third_month_booked_dates = BookingHouseClass.objects.filter(
        holidayhouse_id=holidayhouse_id, day__year=third_year, day__month=third_month
    ).values_list('day__day', flat=True)

    context = {
        'current_year': current_year,
        'current_month': ukrainian_months[current_month],
        'next_month': ukrainian_months[next_month],
        'next_year': next_year,
        'third_month': ukrainian_months[third_month],
        'third_year': third_year,
        'cal_current_month': cal_current_month,
        'cal_next_month': cal_next_month,
        'cal_third_month': cal_third_month,
        'current_month_booked_dates': current_month_booked_dates,
        'next_month_booked_dates': next_month_booked_dates,
        'third_month_booked_dates': third_month_booked_dates,
        'current_day': current_day,
    }

    return context


def holiday_house_1(request):
    context = get_calendar_data(holidayhouse_id=1)
    return render(request, 'mainapp/holiday_house/holiday_house_1.html', context=context)


def holiday_house_2(request):
    context = get_calendar_data(holidayhouse_id=2)
    return render(request, 'mainapp/holiday_house/holiday_house_2.html', context=context)


def holiday_house_3(request):
    context = get_calendar_data(holidayhouse_id=3)
    return render(request, 'mainapp/holiday_house/holiday_house_3.html', context=context)


def holiday_house_4(request):
    context = get_calendar_data(holidayhouse_id=4)
    return render(request, 'mainapp/holiday_house/holiday_house_4.html', context=context)


def holiday_house_5(request):
    context = get_calendar_data(holidayhouse_id=5)
    return render(request, 'mainapp/holiday_house/holiday_house_5.html', context=context)


def holiday_house_6(request):
    context = get_calendar_data(holidayhouse_id=6)
    return render(request, 'mainapp/holiday_house/holiday_house_6.html', context=context)


def holiday_house_7(request):
    context = get_calendar_data(holidayhouse_id=7)
    return render(request, 'mainapp/holiday_house/holiday_house_7.html', context=context)


# def booking(request):
#     weekdays = validWeekday(93)
#     validateWeekdays = isWeekdayValid(weekdays)
#
#     if request.method == 'POST':
#         day = request.POST.get('day')
#         if day is None:
#             messages.success(request, "Будь ласка, виберіть день")
#             return redirect('booking')
#
#         request.session['day'] = day
#         return redirect('bookingSubmit')
#
#     return render(request, 'mainapp/booking.html', {
#         'weekdays': weekdays,
#         'validateWeekdays': validateWeekdays,
#     })


def booking(request):
    weekdays = validWeekday(93)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        day = request.POST.get('day')
        if day is None:
            messages.success(request, "Будь ласка, виберіть день")
            return redirect('booking')

        request.session['day'] = day
        return redirect('bookingSubmit')

    return render(request, 'mainapp/booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })


def bookingSubmit(request):
    user = request.user
    times = ["15:00"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=92)
    maxDate = deltatime.strftime('%Y-%m-%d')
    booking_pets = request.POST.get("booking_pets")
    booking_wish = request.POST.get("booking_wish")

    # Get stored data from django session:
    day = request.session.get('day')

    # Отримуємо доступні будинки на вибрану дату
    holidayhouses = HolidayHouse.objects.exclude(
        id__in=BookingHouseClass.objects.filter(day=day).values_list('holidayhouse_id', flat=True)
    )

    if request.method == 'POST':
        holidayhouse_id = request.POST.get("holidayhouse")
        holidayhouse = HolidayHouse.objects.get(id=holidayhouse_id)
        time = request.POST.get("time")

        if minDate <= day <= maxDate:
            if BookingHouseClass.objects.filter(day=day, holidayhouse=holidayhouse).count() < 1:
                BookingHouseClass.objects.create(
                    user=user,
                    holidayhouse=holidayhouse,
                    day=day,
                    time=time,
                    booking_pets=booking_pets,
                    booking_wish=booking_wish,
                )
                messages.success(request, "Будинок заброньовано! Просимо провести передоплату")
                return redirect('bank_details')
            else:
                messages.success(request, "Вибраний будинок вже заброньовано на цей день!")
        else:
            messages.success(request, "Вибрана дата не відповідає правильному періоду часу!")

    return render(request, 'mainapp/bookingSubmit.html', {
        'times': times,
        'holidayhouses': holidayhouses,
    })


def userPanel(request):
    user = request.user.id
    bookinghouses = BookingHouseClass.objects.filter(user=user).order_by('-day', '-time')
    return render(request, 'mainapp/userPanel.html', {
        'user': user,
        'bookinghouses': bookinghouses,
    })

# def userPanel(request):
#     if request.user.is_authenticated:
#         user = request.user
#         bookinghouses = BookingHouseClass.objects.filter(user=user).order_by('-day', '-time')
#     else:
#         # Handle non-authenticated user case
#         bookinghouses = None  # Or set bookinghouses to an empty list or appropriate default value
#
#     return render(request, 'mainapp/userPanel.html', {
#         'user': user,
#         'bookinghouses': bookinghouses,
#     })

# def userPanel(request):
#     user = request.user
#     if not user.is_authenticated:
#         return render(request, 'mainapp/userPanel.html', {
#             'user': user,
#             'bookinghouses': [],
#             'error_message': 'Спочатку увійдіть!'
#         })
#     bookinghouses = BookingHouseClass.objects.filter(user=user).order_by('-day', '-time')
#     return render(request, 'mainapp/userPanel.html', {
#         'user': user,
#         'bookinghouses': bookinghouses,
#     })


def userUpdate(request, id):
    bookinghouse = get_object_or_404(BookingHouseClass, pk=id)
    userdatepicked = bookinghouse.day
    today = datetime.today()
    # delta24 = userdatepicked >= (today + timedelta(days=1))
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    weekdays = validWeekday(93)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        day = request.POST.get('day')
        request.session['day'] = day
        return redirect('userUpdateSubmit', id=id)

    return render(request, 'mainapp/userUpdate.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'delta24': delta24,
        'id': id,
    })


def userUpdateSubmit(request, id):
    bookinghouse = get_object_or_404(BookingHouseClass, pk=id)
    user = request.user
    times = ["15:00"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=92)
    maxDate = deltatime.strftime('%Y-%m-%d')
    day = request.session.get('day')

    # Отримуємо доступні будинки на вибрану дату
    holidayhouses = HolidayHouse.objects.exclude(
        id__in=BookingHouseClass.objects.filter(day=day).values_list('holidayhouse_id', flat=True)
    )

    if request.method == 'POST':
        holidayhouse_id = request.POST.get("holidayhouse")
        holidayhouse = HolidayHouse.objects.get(id=holidayhouse_id)
        time = request.POST.get("time")

        if minDate <= day <= maxDate:
            if BookingHouseClass.objects.filter(day=day, holidayhouse=holidayhouse).count() < 1 or \
               (bookinghouse.day == day and bookinghouse.holidayhouse == holidayhouse):
                bookinghouse.holidayhouse = holidayhouse
                bookinghouse.day = day
                bookinghouse.time = time
                bookinghouse.save()
                messages.success(request, "Бронювання змінене!")
                return redirect('userPanel')
            else:
                messages.success(request, "Вибраний будинок вже заброньовано на цей день!")
        else:
            messages.success(request, "Вибрана дата не відповідає правильному періоду часу!")

    return render(request, 'mainapp/userUpdateSubmit.html', {
        'times': times,
        'holidayhouses': holidayhouses,
        'id': id,
    })


def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=92)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    # Only show the records 21 days from today
    # Показувати записи лише через 21 день від сьогодні
    items = BookingHouseClass.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')
    profiles = Profile.objects.all()

    return render(request, 'mainapp/staffPanel.html', {
        'items': items,
        'profiles': profiles,
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Loop days you want in the next 90 days:
    # днів циклу, які ви хочете протягом наступних 90 дня:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or \
                y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(weekdays):
    valid_days = []
    for day in weekdays:
        # Якщо є хоча б один будинок, який вільний на цю дату, додаємо дату до валідних
        if HolidayHouse.objects.exclude(
                id__in=BookingHouseClass.objects.filter(day=day).values_list('holidayhouse_id', flat=True)
        ).exists():
            valid_days.append(day)
    return valid_days


def checkEditTime(times, day, id):
    # Only show the time of the day that has not been selected before:
    # Показувати лише той час доби, який раніше не було обрано:
    x = []
    bookinghouse = BookingHouseClass.objects.get(pk=id)
    time = bookinghouse.time
    for k in times:
        if BookingHouseClass.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x

# видалення бронювання через staff-panel

@login_required
def delete_booking(request, id):
    booking = get_object_or_404(BookingHouseClass, id=id)
    if request.user.is_staff:  # Перевірка чи користувач є адміністратором
        booking.delete()
        messages.success(request, "Бронювання успішно видалено!")
    else:
        messages.error(request, "У вас немає дозволу на видалення цього бронювання.")
    return redirect('staffPanel')


# def handling_404(request, exception):
#    return render(request, 'mainapp/404.html', {})

def custom_404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

