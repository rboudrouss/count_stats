echo "do you want to yeet the DataBase ? y/N:"
read conf

if [ $conf = 'y' -o $conf = 'Y' ]; then
    rm db.sqlite3
    echo "DATABASE YOOTED !"
fi

find . -path "API/migrations/*.py" -not -name "__init__.py" -delete
find . -path "API/migrations/*.pyc"  -delete
echo "MIGRATIONS YOOTED ! (making new ones)"
python manage.py makemigrations && python manage.py migrate
echo "yeeting out the program..."