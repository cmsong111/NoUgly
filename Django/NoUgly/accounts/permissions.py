from rest_framework import permissions


# permissions 오버라이드해줌

class IsUserOrReadOnly(permissions.BasePermission):
    # custom된 permission! - >해당 물품은 작성자만 수정할 수 있게끔
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated
    # custom된 permission! - >해당 물품은 작성자만 수정할 수 있게끔

    def has_object_permission(self, request, view, obj):
        # R -> 모든 요청 가능 --> GET, HEAD, OPTIONS request에 대해 허용
        if request.method in permissions.SAFE_METHODS:
            # permissions의 SAFR_METHODS란 우리의 데이터베이스에
            # 영향을 줄 일이 없는 HTTP 요청,
            # 즉 GET, OPTIONS, HEAD를 의미한다!
            return True

        # U와 D는 (그 이외 http 요청) Store의 user만 가능하게한다
        return obj.uIDX == request.user
