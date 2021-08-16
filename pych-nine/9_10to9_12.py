#9-10
from Restaurant import Restaurant
res_1 = Restaurant('miche','china')
res_1.describe_restaurant()
#9-11&&9-12
from privilegers import Admin
jack = Admin('vergil','sparda','none')
jack.describe_user()
jack.privileges.show_privileges()
jack.greet_user()