from app.services.active_directory.connect_to_ad_server import ad_connection
from app.services.password_generator import password_generator

from ldap3 import MODIFY_REPLACE, MODIFY_ADD

class ADUser:
    def __init__(self, user_dn, new_user_attributes, list_group,):
        self.user_dn = user_dn
        self.new_user_attributes = new_user_attributes
        self.list_group = list_group
        self.password = None

    def create(self):
        print(f"В ад створено користувача: {self.new_user_attributes}") # test
        with ad_connection() as connection_to_server:

            connection_to_server.add(self.user_dn, attributes = self.new_user_attributes)

            self.password = password_generator()
            account_password_utf_16_le = f'"{self.password}"'.encode("utf-16-le")

            connection_to_server.modify(
                dn=self.user_dn,
                changes={
                    "unicodePwd": [(MODIFY_REPLACE, [account_password_utf_16_le])],
                    "userAccountControl": [(MODIFY_REPLACE, [512])]
                    # userAccountControl: Числовий битмаск AD.
                    # Значения:
                    # 512 - вмикає звичайний обліковий запис (потребує зміни при першому логіні) (прапор 512 = NORMAL_ACCOUNT)
                    # 544 - вмикає та не потребує зміни паролю при першому вході
                    # 66048 - робить пароль безстроковим
                }
            )

            # Додаємо групи якщо вони є
            if self.list_group:
                for group_dn in self.list_group:
                    connection_to_server.modify(
                        dn = group_dn,
                        changes = {"member": [(MODIFY_ADD, [self.user_dn])]}
                    )
