class BaseTest:
    def setup(self):
        print("Setting up the test")

class LoginTest(BaseTest):  # LoginTest inherits from BaseTest
    def run(self):
        print("Running login test")

class AuditMixin:
    def audit(self, action):
        """Record an audit log for the given action."""
        print(f"Audit log: {action}")

class ExtendedLoginTest(BaseTest, AuditMixin):
    def run(self):
        self.audit("Starting the login test")
        super().setup()
        print("Running extended login test")
        self.audit("Finished the login test")

# Instantiate and use the ExtendedLoginTest
test = ExtendedLoginTest()
test.run()

# Output:
# Audit log: Starting the login test
# Setting up the test
# Running extended login test
# Audit log: Finished the login test
