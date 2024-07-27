from passlib.context import CryptContext

# Define the password context with bcrypt scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.

    :param plain_password: The plain password to verify.
    :param hashed_password: The hashed password to verify against.
    :return: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a password using the bcrypt algorithm.

    :param password: The plain password to hash.
    :return: The hashed password.
    """
    return pwd_context.hash(password)
