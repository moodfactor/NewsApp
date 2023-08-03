import asyncio
import requests


async def book_appointment(tutor_list, date):
    # Make a POST request to httpbin.org with the date
    post_data = {
        'date': date
    }
    response = await requests.post('https://httpbin.org/post', data=post_data)

    # Get the response from httpbin.org
    get_data = await response.json()

    # Print the response to the terminal for debugging
    print(f'Response from httpbin.org: {get_data}')

    # Return the response
    return get_data

async def main():
    # List of tutors and their available times
    tutor_list = [
        {'name': 'Tutor 1', 'times': ['Mon', 'Wed', 'Fri']},
        {'name': 'Tutor 2', 'times': ['Tue', 'Thu']},
        {'name': 'Tutor 3', 'times': ['Sat', 'Sun']}
    ]

    # Create a web application that allows clients to book appointments
    web_app = web.Application()

    @web_app.route('/book', methods=['POST'])
    async def book(request):
        # Get the date from the request body
        date = request.json()['date']

        # Book the appointment with the tutor
        tutor_data = book_appointment(tutor_list, date)

        # Return the response
        return web.Response(text=tutor_data)

    # Start the web application
    web_app.run(port=8000)

asyncio.run(main())