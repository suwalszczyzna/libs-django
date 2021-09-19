import dataclasses

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from services.site_info import SiteInfoService, FavIconGrabber, SiteInfoResponse


@api_view(['GET'])
def site_meta_info(request):
    url = request.GET.get('url')
    if not url:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        info_service = SiteInfoService(url)
        data = info_service.get_meta_info()
        return Response(data=data.__dict__, status=status.HTTP_200_OK)
    except (NotFound, ValueError):
        not_found_data = SiteInfoResponse(title="Page not found", description="", base_url="")
        return Response(status=status.HTTP_200_OK, data=not_found_data.__dict__)


@api_view(['GET'])
def site_favicon(request):
    url = request.GET.get('url')
    if not url:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    min_icon_size = request.GET.get('min_icon_size') or 40
    favicon_grabber = FavIconGrabber(url)

    try:
        data = {
            "icon": favicon_grabber.get_icon(min_icon_size)
        }
        return Response(data=data, status=status.HTTP_200_OK)
    except NotFound as e:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": e.detail})
