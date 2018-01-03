# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    db.connection.commit()
#    assert len(old_groups) + 1 == len(db.get_group_list()) # count used as a hash function for preliminary check

    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#    а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я
