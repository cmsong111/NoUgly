package com.gdsc.nougly

import android.app.DatePickerDialog
import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.ImageButton
import android.widget.TextView
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.chip.Chip
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.util.*


class Register : AppCompatActivity() {

    //날짜 전역 변수 선언
    var dateString = ""
    //성별 전역 변수 선언
    var gender:String?= null
    //회원가입 성공했는지 값 전역변수 선언
    var registerSuccess:String?= null

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.register)

        //선언 파트
        val editTextID = findViewById<EditText>(R.id.idEditText) //EditText 컴포넌트를 찾아서 editTextPw 변수에 저장한다.
        val editTextPW = findViewById<EditText>(R.id.pwEditText) //비밀번호 선언
        val editTextREPW = findViewById<EditText>(R.id.repwEditText) //비밀번호 2번째
        val editTextNAME = findViewById<EditText>(R.id.nameEditText) //이름
        val editTextPHONENUM = findViewById<EditText>(R.id.phoneEditText) //휴대 전화 번호
        val editTextAddress = findViewById<EditText>(R.id.addressEditText) //주소

        //retrofit
        var retrofit = Retrofit.Builder()
            .baseUrl("https://cmsong111.pythonanywhere.com/rest-auth/registration/") //해당 링크
            .addConverterFactory(GsonConverterFactory.create()) //Gson 사용 선언
            .build() //객체 생성

        //Django에 넣을 POST 발행 소스
        var RegisterService = retrofit.create(RegisterService::class.java)


        //달력 버튼을 눌렀을 시에
        findViewById<ImageButton>(R.id.birthdayButton).setOnClickListener {

            val cal = Calendar.getInstance()    //캘린더뷰 만들기

            //클릭한 날짜를 받아와서 저장하기
            val dateSetListener = DatePickerDialog.OnDateSetListener { view, year, month, dayOfMonth ->
                dateString = "${year}-${month}-${dayOfMonth}"
                findViewById<TextView>(R.id.birthdayTextView).text = "생일 : "+dateString
                Log.d("Date", dateString)
            }
            DatePickerDialog(this, dateSetListener, cal.get(Calendar.YEAR),cal.get(Calendar.MONTH),cal.get(Calendar.DAY_OF_MONTH)).show()

        }


        //여성 버튼 클릭시
        findViewById<Chip>(R.id.femaleChip).setOnClickListener{
            gender = "여"
        }

        //남성 버튼 클릭시
        findViewById<Chip>(R.id.maleChip).setOnClickListener{
            gender = "남"
        }

        //회원가입하기 버튼 클릭시
        findViewById<Button>(R.id.SignUpButton).setOnClickListener {

            val idText = editTextID.text.toString()
            val passwordText =
                editTextPW.text.toString() //editTextPw 에서 사용자가 입력한 텍스트를 불러와 passwordText 에 저장한다.
            val repwText = editTextREPW.text.toString()
            val nameText = editTextNAME.text.toString()
            val phoneText = editTextPHONENUM.text.toString()
            val birthText = dateString
            val genderText = gender
            val addressText = editTextAddress.text.toString()

            //통신 과정 소스 - 결과보여주기 위해 RegisterOutput과 연결
            RegisterService.requestRegister(idText, passwordText, repwText, nameText, phoneText, birthText, genderText, addressText).enqueue(object : Callback<RegisterOutput> {
                override fun onResponse(call: Call<RegisterOutput>, response: Response<RegisterOutput>) {

                    var register = response.body()

                    if(register != null && response.isSuccessful){
                        registerSuccess = "1"
                    } else{
                        var testdialog = AlertDialog.Builder(this@Register)
                        testdialog.setTitle("알람")
                        testdialog.setMessage("id : " + idText + "\npw : " + passwordText + "\nrepw : " + repwText + "\nname :" + nameText + "\nphone : " + phoneText
                                + "\nbirth : " + birthText + "\ngener : " + genderText + "\naddress : " + addressText)
                        testdialog.show()
                        Log.d("Error Code Test", response.errorBody()?.string()!!)
                    }


                    var dialog = AlertDialog.Builder(this@Register)
                    dialog.setTitle("알람")
                    dialog.setMessage("user : " + register?.user + "\ntoken : " + register?.token)//?는 Null값이 있을 수 있어서
                    dialog.show()
                    Log.d("debug", "Dialog")

                    if(register?.token != null) {
                        registerSuccess = "1"
                        //알림창으로 Django값 확인

                    }
                }

                override fun onFailure(call: Call<RegisterOutput>, t: Throwable) {
                    Log.d("Debug", t.message.toString())

                    var dialog = AlertDialog.Builder(this@Register)
                    dialog.setTitle("통신실패")
                    dialog.setMessage("통신에 실패를 하였습니다.")
                    dialog.show()

                    call.cancel()
                }

            })

            if(registerSuccess == "1"){
                val loginintent = Intent(this,Login::class.java) //로그인 화면 불러옴
                startActivity(loginintent)
                this.finish()
            }

        }

    }

}