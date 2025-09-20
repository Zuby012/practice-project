class UserNameData:
    def __init__(self, username, firstname, lastname, email):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def _reg(self, body, re):
        """
        Arg:
            body: array to contain messages for users if form isn't feeled correctly
            re: regex module
        """

        if self.firstname is False or self.lastname is False or self.username is False or self.email is False:
            body.append('please fill all required field<br>')
        if bool(re.match(r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email)) is False:
            body.append('your email is not correct<br>')


class PasswordData:
    def __init__(self, password, confirm_pass):
        self.password = password
        self.confirm_pass = confirm_pass

    def _reg(self, body, re):
        """
        Arg:
            body: array to contain messages for users if form isn't feeled correctly
            re: regex module
        """
        if self.password != self.confirm_pass:
            body.append('your passwords do not match')
        if len(self.password) < 8:
            body.append('your passwords is to short')
        if bool(re.search(r'[a-zA-Z]', self.password)) is False or bool(re.search(r'\d', self.password)) is False or bool(re.search(r'[^\w\s]', self.password)) is False:
            body.append('your passwords is to short')


class OtherData:
    def __init__(self, dob, tel, gender, nationality):
        self.dob = dob
        self.tel = tel
        self.gender = gender
        self.nationality = nationality

    def _reg(self, body, re):
        """
        Arg:
            body: array to contain messages for users if form isn't feeled correctly
            re: regex module
        """
        if bool(re.search(r'\d', self.tel)) is False:
            body.append('invalid phone number')


def reg(request_obj):
    nameobj = UserNameData(
        request_obj.form['username'],
        request_obj.form['firstname'],
        request_obj.form['lastname'],
        request_obj.form['email'])
