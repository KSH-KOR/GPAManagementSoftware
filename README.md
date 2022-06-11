# CatFoodCalorieCalculator
What does this project do? 
  This software display how much amount of calorie your cat need to take depending on your cat's type and weight.

Why is this project useful? 
  Feeding proper amount of food is very important for your cat's health. If you use this software, you can know how much you need to feed.

How to get started?
  1.clone this github
  2.put this folder on your server directory (for example, under /var/www/html/)
  1.install module
    pip install os-sys (os-sys 2.1.4)
    pip install python-wordpress-xmlrpc (python-wordpress-xmlrpc 2.3)
    pip install pandas (pandas 1.4.2)
    pip install numpy (numpy 1.22.4)
  2.clone this repository
    git clone 
    
  4.edit driver.py file
    16 lines: client = Client('your_wordpress_url', 'wordpress id', 'wordpress password')
    (for example: client = Client('http://localhost/wp/xmlrpc.php', 'id123', 'password123'))
  5-1.run submit.html file which is located under GPAManagementSoftware\src\templates
  5-2.or copy and paste submit.html script on your wordpress page as html script
  6.put your hisnet id and password on html form and hit login button
  7.check your wordpress post

Where can people get more help, if needed? Presentation Video (YouTube) Link
  
Clearly indicate what your contribution to your project is. (This is very important.)
  
