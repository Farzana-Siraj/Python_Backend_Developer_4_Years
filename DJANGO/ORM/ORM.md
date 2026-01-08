## Relationships
| Relationship        | Django Field         | Use Case         | |
| ------------------- | -------------------- | ---------------- |--|
| One-to-One          | `OneToOneField`      | User ↔ Profile   | One object is linked to only one object |
| One-to-Many         | `ForeignKey`         | Author ↔ Books   | One object can be linked to many objects |
| Many-to-Many        | `ManyToManyField`    | Student ↔ Course | Many objects can be related to many other objects |
| Many-to-Many + data | `through`            | Enrollment       |
| Self-relation       | `ForeignKey('self')` | Category tree    | A model related to itself |
| Polymorphic         | `GenericForeignKey`  | Comments, Likes  | One model can relate to multiple different models |

#### Foreign Key and One to One
ForeignKey creates a one-to-many relationship, while OneToOneField creates a one-to-one relationship with a unique constraint on the foreign key.

| Feature           | ForeignKey                   | OneToOneField      |
| ----------------- | ---------------------------- | ------------------ |
| Relationship      | One-to-Many                  | One-to-One         |
| Unique constraint | ❌ No                         | ✅ Yes              |
| DB column         | FK                           | FK + UNIQUE        |
| Reverse access    | `department.employee_set`    | `user.userprofile` |
| Use case          | Categories, Orders, Comments | Profile, Settings  |
|                   |One parent → many children|Exactly one related record|

- Foreign key column has a UNIQUE constraint
```bash
# foreignkey
department.employee_set.all()
# one-to-one
user.userprofile

```