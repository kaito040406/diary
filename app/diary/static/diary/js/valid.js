onload = function () {
  const form = document.getElementById("form");
  //form element
  var name = document.getElementById("id_user_name");
  if (name == null) {
    name = document.getElementById("id_commenter");
  }
  var article = document.getElementById("id_article");
  if (article == null) {
    article = document.getElementById("id_comment");
  }

  const name_error_message = document.getElementById("name-error-message");
  const article_error_message = document.getElementById(
    "article-error-message"
  );

  const btn = document.getElementById("btn");

  //バリデーションパターン
  const nameExp = /^.{1,10}$/;
  const articleExp = /^[\s\S]{1,700}$/;
  //初期状態設定
  btn.disabled = true;

  //event

  //name
  name.addEventListener("keyup", (e) => {
    if (nameExp.test(name.value)) {
      name.setAttribute("class", "success");
      name_error_message.style.display = "none";
    } else {
      name.setAttribute("class", "error");
      name_error_message.style.display = "block";
    }
    console.log(name.getAttribute("class").includes("success"));
    checkSuccess();
  });

  //article
  article.addEventListener("keyup", (e) => {
    if (articleExp.test(article.value)) {
      article.setAttribute("class", "success");
      article_error_message.style.display = "none";
    } else {
      article.setAttribute("class", "error");
      article_error_message.style.display = "block";
    }
    console.log(article.getAttribute("class").includes("success"));
    checkSuccess();
  });

  //ボタンのdisabled制御
  const checkSuccess = () => {
    if (name.value && article.value) {
      if (
        name.getAttribute("class").includes("success") &&
        article.getAttribute("class").includes("success")
      ) {
        btn.disabled = false;
      } else {
        btn.disabled = true;
      }
    } else {
      btn.disabled = true;
    }
  };
};
