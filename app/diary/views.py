from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import job_m_category
from .models import job_t_diary
from .models import job_t_comment
from datetime import datetime
from .forms import DiaryForm
from .forms import nameForm
from .forms import CommentForm
from .forms import CommnterName

# from diary.lib import analysis

# Create your views here.
def index(request):
  diaries = job_t_diary.objects.order_by('create_day')#日誌データを取得
  params={
    'diaries':diaries
  }
  return render(request, 'diary/index.html', params)

def show(request, num):
  diary = job_t_diary.objects.get(id=num)
  comments = job_t_comment.objects.filter(comment_diary_id=num).order_by('create_day')
  name = CommnterName()
  commentForm = CommentForm()
  params={
    'diary':diary,
    'comments':comments,
    'nameForm':name,
    'commentForm':commentForm
  }
  # 何時間前の機能をつける
  return render(request, 'diary/show.html',params)

def create(request):
  categories = job_m_category.objects.all()
  name = nameForm()
  Diary = DiaryForm()
  params={
    'categories':categories,
    'nameForm':name,
    'diaryForm':Diary
  }
  return render(request, 'diary/create.html', params)


def diaryForm(request):
  try:
    category_id = int(request.POST['category_id'])
    category = job_m_category.objects.get(id=category_id)
    userName = request.POST['user_name']#非ログイン時は入力した名前
    body = request.POST['article']
    user_id = 0 #非ログイン時のuser_idは0となる
    title = '日直日誌'
    createDay = datetime.now()
    diaryDate = job_t_diary(writer_name = userName, user_id=user_id, title=title, diary=body, category_id=category, create_day=createDay ,delete_frg=0, like_number=0, comment_number=0)
    diaryDate.save()
    return redirect(to='/diary')
  except Exception as e:
    return HttpResponse("システムエラー発生")

def commentForm(request, num):
  commenterName = request.POST['commenter']
  comment = request.POST['comment']
  user_id = 0
  diary_id = job_t_diary.objects.get(id=num)
  createDay = datetime.now()
  commentLength = int(diary_id.comment_number) + 1
  commentDate = job_t_comment(commenter_name = commenterName, user_id = user_id, comment = comment, delete_frg = 0, comment_diary_id = diary_id, create_day = createDay)
  commentDate.save()
  diary_id.comment_number = commentLength
  diary_id.save()
  response = redirect('/diary/show/'+str(num))
  return response