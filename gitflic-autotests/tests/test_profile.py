from pages.profile_page import ProfilePage
import faker
import config
import pytest


Faker = faker.Faker()
first_name = Faker.first_name()
last_name = Faker.last_name()
full_name = f"{first_name} {last_name}"


def test_change_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page('Sergey D')
    profile.update_profile(first_name, last_name)
    profile.open_profile_page('Sergey D')

    assert profile.get_user_name() == full_name, "имя профиля не было обновленно"

def test_check_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page('Sergey D')
    name = profile.get_user_name()

    assert name != "", "Имя профиля должно быть не пустое"
    assert len(name) > 0, "Имя профиля содержит хотябы один символ"
