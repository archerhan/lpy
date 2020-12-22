
import redis

def main():
    client = redis.Redis(host='123.57.130.195',port=6379, password='123456')
    client.set('username', 'admin')
    client.hset('student', 'name', 'archer')
    client.hset('student', 'age', 40)
    client.keys('*')

    client.get('username')
    client.hgetall('student')


if __name__ == '__main__':
    main()