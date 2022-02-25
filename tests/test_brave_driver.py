import os

import pytest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


def test_driver_with_ssl_verify_disabled_can_be_downloaded(ssl_verify_enable):
    os.environ['WDM_SSL_VERIFY'] = '0'
    custom_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "ssl_disabled",
    )
    driver_path = ChromeDriverManager(
        version="83.0.4103.39",
        path=custom_path,
        chrome_type=ChromeType.BRAVE,
    ).install()

    assert os.path.exists(driver_path)


def test_BRAVE_manager_with_specific_version():
    bin_path = ChromeDriverManager("2.27", chrome_type=ChromeType.BRAVE).install()
    assert os.path.exists(bin_path)


def test_driver_can_be_saved_to_custom_path():
    custom_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "custom")

    path = ChromeDriverManager(version="2.27", path=custom_path,
                               chrome_type=ChromeType.BRAVE).install()
    assert os.path.exists(path)
    assert custom_path in path


def test_BRAVE_manager_with_wrong_version():
    with pytest.raises(ValueError) as ex:
        ChromeDriverManager("0.2", chrome_type=ChromeType.BRAVE).install()
    assert "There is no such driver by url" in ex.value.args[0]


@pytest.mark.parametrize('os_type', ['win32', 'win64'])
def test_can_get_BRAVE_for_win(os_type):
    path = ChromeDriverManager(version="83.0.4103.39", os_type=os_type,
                               chrome_type=ChromeType.BRAVE).install()
    assert os.path.exists(path)
