# Task 2 This functrion is simply for the conversion of c to f
def convert_the_weather():
    '''Convert temperature in °F to °C and print results'''
    
    while True:

        # Task 1
        uzer_input = input("Enter the present temperature in °F (or type 'done' to exit): ").strip()

        # Task 2b
        try:
            if uzer_input.lower() == 'done':
                print("You're all done!:)")
                break
            convert_2_int = int(uzer_input)
            convert_temp = (convert_2_int - 32) * 5 / 9
            print(f"The temperature outside is {convert_temp:.2f}°C")
        except ValueError:
            print("Invalid response. Don't spell the numbers. Enter digits.")