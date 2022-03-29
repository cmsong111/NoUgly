package com.gdsc.nougly

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class Login : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState) //화면 제작
        setContentView(R.layout.login) //로그인 xml 연결

        //id, pw 선언
        val editTextID = findViewById<EditText>(R.id.IdEditText) //EditText 컴포넌트를 찾아서 editTextPw 변수에 저장한다.
        val editTextPW = findViewById<EditText>(R.id.PwEditText) //비밀번호 선언

        //retrofit
        var retrofit = Retrofit.Builder()
            .baseUrl("https://cmsong111.pythonanywhere.com/rest-auth/login/") //해당 링크
            .addConverterFactory(GsonConverterFactory.create()) //Gson 사용 선언
            .build() //객체 생성

        //Django에 넣을 POST 발행 소스
        var loginService = retrofit.create(LoginService::class.java)

        //서비스 내에선 Intent 관리가 안되기 때문에 변경 가능한 변수 선언
        var loginSuccess:String?= null

        //로그인 버튼을 클릭시
        findViewById<Button>(R.id.SignInButton).setOnClickListener {
            val idText = editTextID.text.toString()
            val passwordText =
                editTextPW.text.toString() //editTextPw 에서 사용자가 입력한 텍스트를 불러와 passwordText 에 저장한다.

            //통신 과정 소스 - 결과보여주기 위해 LoginOutput과 연결
            loginService.requestLogin(idText, passwordText).enqueue(object : Callback<LoginOutput> {
                override fun onResponse(call: Call<LoginOutput>, response: Response<LoginOutput>) {
                    //통신이 성공했을 때 - 응답값을 따옴

                    var login = response.body()

                    if(login?.user?.email == idText) {
                        if(login?.token != null) {
                            loginSuccess = "1"
                        }
                    } else { //아이디 또는 비밀번호를 잘못쳤을 때
                        loginSuccess = "2"
                    }

                }

                override fun onFailure(call: Call<LoginOutput>, t: Throwable) {
                    //통신이 실패했을 때
                    Log.d("Debug", t.message.toString())

                    var dialog = AlertDialog.Builder(this@Login)
                    dialog.setTitle("통신실패")
                    dialog.setMessage("통신에 실패를 하였습니다.")
                    dialog.show()

                    call.cancel()
                }
            })

            //로그인 상황 확인
            if(loginSuccess == "1"){
                Log.d("loginSuccess","로그인 성공!!")
                val mainintent = Intent(this, Main::class.java) //성공시 main 화면 불러오기
                startActivity(mainintent) //액티비티 실행
                this.finish() //이전 화면 종료
            }else if (loginSuccess == "2"){
                findViewById<TextView>(R.id.wrongTextView).text="아이디 또는 비밀번호가 틀렸어요. 다시 입력해주세요."
            }
        }//로그인 버튼 종료


        //회원가입 버튼 클릭시
        findViewById<TextView>(R.id.RegisterEditText).setOnClickListener {
            val registerintent = Intent(this,Register::class.java) //회원가입 화면 불러옴
            startActivity(registerintent)
            this.finish()
        }//회원가입 버튼 정료

    }

}