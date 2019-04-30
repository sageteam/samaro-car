from django.utils.translation import gettext as _

class MainTypes:

    def __init__(self, is_charfield = False, *args, **kwargs):
        
        if is_charfield:
            self.PRIMARY = 'p'
            self.INFO = 'i'
            self.SUCCESS = 's'
            self.DANGER = 'd'
            self.DEFAULT = 'f'
            self.WARNING = 'w'
        
        self.DEFAULT = 0
        self.PRIMARY = 1
        self.INFO = 2
        self.SUCCESS = 3
        self.DANGER = 4
        self.WARNING = 5

    def get_types(self):
        types = (
            (self.DEFAULT, 'draft'),
            (self.PRIMARY, 'primary'),
            (self.INFO, 'info'),
            (self.SUCCESS, 'success'),
            (self.DANGER, 'danger'),
            (self.WARNING, 'warning'),
        )
    
        return types


    def is_default(self, value):
        return self.DEFAULT == value

    def is_primary(self, value):
        return self.PRIMARY == value

    def is_info(self, value):
        return self.INFO == value
    
    def is_success(self, value):
        return self.SUCCESS == value
    
    def is_danger(self, value):
        return self.DANGER == value
    
    def is_warning(self, value):
        return self.WARNING == value

class PostableStatus:
    def __init__(self, is_charfield = False, *args, **kwargs):
        if is_charfield:
            self.DRAFT = 'd'
            self.PUDBLISHED = 'p'

        self.DRAFT = 0
        self.PUDBLISHED = 1
    

    def is_draft(self, value):
        return self.DRAFT == value
    

    def is_published(self, value):
        return self.PUDBLISHED == value
    

    def get_status(self):
        status = (
            (self.DRAFT, 'Draft'),
            (self.PUDBLISHED, 'Published'),
        )
        return status


class DegreeLevel:
    PHD = 7
    DR = 6
    PHD_STD = 5
    MSC = 4
    MSC_STD = 3
    BACHELOR = 2
    BACHELOR_STD = 1
    
    @classmethod
    def choices(cls):
        result = (
            (cls.PHD, _('PH.D.')),
            (cls.DR, _('Doctor')),
            (cls.PHD_STD, _('PHD student')),
            (cls.MSC, _('MSc')),
            (cls.MSC_STD, _('MSc student')),
            (cls.BACHELOR, _('Bachelor')),
            (cls.BACHELOR_STD, _('Bachelor student')),
        )

        return result

class ScientificRate:
    PROFESSOR = 4
    ASSOCIATE_PROFESSOR = 3
    ASSISTANT_PROFESSOR = 2
    TEACHER = 1
    OTHER = 0
    
    @classmethod
    def choices(cls):
        result = (
            (cls.PROFESSOR, _('Professor')),
            (cls.ASSOCIATE_PROFESSOR, _('Associate Professor')),
            (cls.ASSISTANT_PROFESSOR, _('Assistant Professor')),
            (cls.TEACHER, _('Teacher')),
            (cls.OTHER, _('other')),
        )

        return result

class PersonLegality:
    REAL = 1
    LEGAL = 2

    @classmethod
    def choices(cls):
        result = (
            (cls.REAL, _('Real Person')),
            (cls.LEGAL, _('Legal Person')),
        )

        return result
    
class UserTypes:
    STUDENT = 1
    TEAM = 2
    REFEREE = 3
    SPONSOR = 4

    @classmethod
    def choices(cls):
        result = (
            (cls.STUDENT, _('Student')),
            (cls.TEAM, _('Team')),
            (cls.REFEREE, _('Referee')),
            (cls.SPONSOR, _('Sponsor')),
        )

        return result
    