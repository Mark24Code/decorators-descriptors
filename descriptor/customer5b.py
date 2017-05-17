"""
A client with name and e-mail:

    >>> jack = Customer('John Robinson', 'jack@rob.org')
    >>> jack.full_email()
    'John Robinson <jack@rob.org>'

A client cannot be created with a blank e-mail:

    >>> joe = Customer('Joseph Blow', '')
    Traceback (most recent call last):
      ...
    ValueError: 'email' must not be empty
    >>> joe = Customer('Joseph Blow', 'joe@blow.up')
    >>> joe.full_email()
    'Joseph Blow <joe@blow.up>'

Assigning a blank e-mail later is not allowed either:

    >>> joe.email = ''
    Traceback (most recent call last):
      ...
    ValueError: 'email' must not be empty

`NonBlank` fields must also be strings:

    >>> dummy = Customer('Buster', 99)
    Traceback (most recent call last):
      ...
    TypeError: 'email' must be of type 'str'

The `NonBlank` field values are stored in properly named
`Customer` instance attributes:

    >>> for key, value in sorted(jack.__dict__.items()):
    ...     print('{:>10} : {!r}'.format(key, value))
         email : 'jack@rob.org'
      fidelity : 0
          name : 'John Robinson'

"""

from model5b import named_fields, NonBlank


@named_fields
class Customer:

    name = NonBlank()
    email = NonBlank()

    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    def full_email(self):
        return '{0} <{1}>'.format(self.name, self.email)
