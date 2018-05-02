# -*- coding: utf-8 -*-
# Subject to the terms of the GNU AFFERO GENERAL PUBLIC LICENSE, v. 3.0. If a copy of the AGPL was not
# distributed with this file, You can obtain one at http://www.gnu.org/licenses/agpl.txt
#
# Author: Davide Galletti                davide   ( at )   c4k.it

from django.shortcuts import get_object_or_404
from ap.models import Application


def play(request, application_id):
    application = get_object_or_404( Application, pk=application_id )
    application.workflows