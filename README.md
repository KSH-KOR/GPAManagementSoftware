# CatFoodCalorieCalculator
What does this project do? <br />
>This software display how much amount of calorie your cat need to take depending on your cat's type and weight.

Why is this project useful? <br />
>Feeding proper amount of food is very important for your cat's health. If you use this software, you can know how much you need to feed.

How to get started?<br />
1. install module<br />
>>pip install os-sys (os-sys 2.1.4)<br />
>>pip install python-wordpress-xmlrpc (python-wordpress-xmlrpc 2.3)<br />
>>pip install pandas (pandas 1.4.2)<br />
>>pip install numpy (numpy 1.22.4)<br />
2. clone this repository<br />
>>git clone https://github.com/KSH-KOR/cat_food.git <br />
3. move wordpress module to the src directory<br />
>>sudo cp -R /home/"user_name"/.local/lib/python3.9/site-packages/wordpress_xmlrpc cat_food/src<br />
4. copy the repository under your server directory (for example, under /var/www/html/)<br />
>>sudo cp -R ./cat_food /usr/www/html/<br />
5. edit post.py file<br />
>>sudo chmod 666 post.py<br />
>>sudo vim post.py<br />
>>>line 9: client = Client('your_wordpress_url', 'wordpress id', 'wordpress password')<br />
>>>(for example: client = Client('http://localhost/wp/xmlrpc.php', 'id123', 'password123'))<br />
6. run submit.html file which is located under cat_food\src\templates<br />
7. or copy and paste submit.html script on your wordpress page as html script<br />
>>and modify form action="exec_py.php directory"<br />
8. fill the html form as the instructions<br />
9. check your wordpress post<br />

Where can people get more help, if needed? Presentation Video (YouTube) Link<br />
  
Clearly indicate what your contribution to your project is. (This is very important.)<br />
  
