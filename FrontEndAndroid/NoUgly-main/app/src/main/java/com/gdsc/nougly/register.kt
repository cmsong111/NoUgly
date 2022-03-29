package com.gdsc.nougly

import android.app.DatePickerDialog
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageButton
import android.widget.TextView
import com.google.android.material.chip.Chip
import java.util.*

class register : AppCompatActivity() {

    var dateString = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.register)

        //달력 버튼을 눌렀을 시에
        findViewById<ImageButton>(R.id.birthdayButton).setOnClickListener {
            val cal = Calendar.getInstance()    //캘린더뷰 만들기

            //클릭한 날짜를 받아와서 저장하기
            val dateSetListener = DatePickerDialog.OnDateSetListener { view, year, month, dayOfMonth ->
                dateString = "${year}년 ${month+1}월 ${dayOfMonth}일"
                findViewById<TextView>(R.id.birthdayTextView).text = "생일 : "+dateString
            }
            DatePickerDialog(this, dateSetListener, cal.get(Calendar.YEAR),cal.get(Calendar.MONTH),cal.get(Calendar.DAY_OF_MONTH)).show()
        }

        //칩 버튼을 눌렀을 시에
        //findViewById<Chip>(R.id.femaleChip).setOnClickListener{

        //}

        findViewById<ImageButton>(R.id.SignUpButton).setOnClickListener {
            val loginintent = Intent(this,Login::class.java) //로그인 화면 불러옴
            startActivity(loginintent)
            this.finish()
        }

    }

}