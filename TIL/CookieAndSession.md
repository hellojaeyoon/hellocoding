

---

쿠방에서 개발자도구로 cookies에 들어가 sid 삭제하면 저장되었던 상태들이 사라짐

ex) 장바구니에 담고 cookies에 있는 sid를 삭제시 장바구니 내에 저장했던 기록이 사라짐

### http 쿠키는 상태가 있는 세션을 만들도록 해준다

signup : 유저 create

login: 세션 create!



생활코딩 -> 쿠키, 세션 복습

---

1. /accounts/
   - 유저 목록을 출력하는 페이지를 나타낸다.

```python
# accounts/views.py
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    members = User.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'accounts/index.html', context)
```

