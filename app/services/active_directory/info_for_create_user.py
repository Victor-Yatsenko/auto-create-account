from app.services.active_directory.ad_user import ADUser

new_user_attributes = {
    "objectClass": ["top", "person", "organizationalPerson", "user"],
    "sAMAccountName": "i.ivanov",
    "givenName": "Иван",
    "sn": "Иванов"
}

create = ADUser(None, new_user_attributes = new_user_attributes)

create.create()