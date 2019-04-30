def roles():
    MEMBER = 1
    GENIUES = 2
    SUPERVISOR = 3
    EXECUTOR = 4
    ROLE_CHOICES = (
        (MEMBER, 'Member'),
        (GENIUES, 'Genius'),
        (SUPERVISOR, 'SuperVisor'),
        (EXECUTOR, 'Executor'),
    )

    return ROLE_CHOICES

def main_types():
    DEFAULT = 0
    PRIMARY = 1
    SUCCESS = 2
    INFO = 3
    WARNING = 4
    DANGER = 5

    MAIN_TYPES = (
        (DEFAULT, 'default'),
        (PRIMARY, 'primary'),
        (SUCCESS, 'success'),
        (INFO, 'info'),
        (WARNING, 'warning'),
        (DANGER, 'danger'),
    )

    return MAIN_TYPES

def order_status():
    WAITING = 1
    DONE = 2
    IN_PROGRESS = 3

    ORDER_STATUS = (
        (WAITING, 'منتظر بمانید'),
        (DONE, 'تحویل داده شد'),
        (IN_PROGRESS, 'در حال انجام')
    )

    return ORDER_STATUS


def post_status():
    PUBLISH = 1
    DRAFT = 0

    POST_STATUS = (
        (PUBLISH, 'Publish'),
        (DRAFT, 'Draft'),
    )

    return POST_STATUS