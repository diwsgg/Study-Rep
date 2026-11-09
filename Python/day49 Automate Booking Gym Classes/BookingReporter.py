class BookingReporter:
    #why use @staticmethod
    #the function doesn't need self because it doesn't access any attributes of a BookingReporter object.
    @staticmethod
    def summary(processed_classes, total_target_classes):

        new_bookings = sum(
            c['status'] == 'New Booking'
            for c in processed_classes
        )

        new_waitlists = sum(
            c['status'] == 'New Waitlist'
            for c in processed_classes
        )

        already_processed = sum(
            c['status'] in (
                'Already Booked',
                'Already Waitlisted'
            )
            for c in processed_classes
        )

        print('\n--- BOOKING SUMMARY ---')

        print(f'Classes booked: {new_bookings}')
        print(f'Waitlists joined: {new_waitlists}')
        print(f'Already booked/waitlisted: {already_processed}')

        print(
            f'Total Tuesday & Thursday 6pm classes: '
            f'{total_target_classes}'
        )

        print('\n--- DETAILED CLASS LIST ---')

        for class_info in processed_classes:

            print(
                f'  • [{class_info["status"]}] '
                f'{class_info["class"]} Class on '
                f'{class_info["date"]}'
            )

        return len(processed_classes)
    #as before we do not need any attribute 
    @staticmethod
    def verify(number_booking, expected_bookings):

        print('\n--- VERIFICATION RESULT ---')

        print(f'Expected: {expected_bookings} bookings')
        print(f'Found: {number_booking} bookings')

        if number_booking < expected_bookings:

            missing = expected_bookings - number_booking

            print(f'❌ MISMATCH: Missing {missing} bookings')

        elif number_booking > expected_bookings:

            extra = number_booking - expected_bookings

            print(f'⚠️ MISMATCH: Found {extra} extra bookings')

        else:
            print('✅ SUCCESS: All bookings verified!')