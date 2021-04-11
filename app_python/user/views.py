import datetime as dt
import logging
import pytz
from datetime import *
from time import strftime, localtime

from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer


def utc_offset_string(epoch_time, timezone=None):
    """==========================================================================
       Get the utc offset (example:+01:00) from the unix epoch time
       see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
       for timezone.
    =========================================================================="""
    if timezone:
        tz = pytz.timezone(timezone)
    else:
        tz = pytz.timezone('Europe/Paris')

    dt_record = dt.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(tz)
    offset_seconds = dt_record.utcoffset().total_seconds()
    offset_hours = offset_seconds / 3600
    z = offset_hours

    if z > 0:
        z = "+{:g}".format(z)
    else:
        z = "{:g}".format(z)

    return z


class TimestampFormatter(logging.Formatter):
    """==========================================================================
        Format timestamp with [year]-[month]-[day]T[hour]:[minute]:[second].[microseconds]+[utc offset]
    =========================================================================="""
    converter = dt.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%dT%H:%M:%S.%f")
            z = utc_offset_string(record.created)
            s = "%s%s" % (t, z)
        return s


def generate_logger():
    """logger with timestamp format with utc offset"""
    logger = logging.getLogger('UserLogger')
    logger.setLevel(logging.DEBUG)
    message_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = TimestampFormatter(fmt=message_format)
    if not len(logger.handlers):
        file_handler = logging.FileHandler('log/trailerplan-users.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_queryset(self):
        logger = generate_logger()
        if self.action == 'retrieve':
            idStr = self.kwargs.get('pk')
            idpk = int(idStr)

            logger.debug('get user with id {}'.format(idStr))
            logger.info('get user with id {}'.format(idStr))
            logger.warning('get user with id {}'.format(idStr))
            logger.error('get user with id {}'.format(idStr))
            logger.critical('get user with id {}'.format(idStr))

            return User.objects.filter(id=idpk)
        else:
            logger.debug('get all users order by lastName')
            logger.info('get all users order by lastName')
            logger.warning('get all users order by lastName')
            logger.error('get all users order by lastName')
            logger.critical('get all users order by lastName')

            return User.objects.order_by('lastName')
