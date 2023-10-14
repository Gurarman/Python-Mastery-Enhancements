from controller.main_controller import MainController

if __name__ == '__main__':
    """
    Main entry point of the Travel Records Management System application.

    When the script is run as the main module, an instance of MainController is created
    and its run method is called to start the application.
    """
    controller = MainController()
    controller.run()
