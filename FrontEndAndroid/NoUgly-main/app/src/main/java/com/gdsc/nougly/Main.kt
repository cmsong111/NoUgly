package com.gdsc.nougly

import android.content.ContentValues.TAG
import android.os.Bundle
import android.transition.ChangeBounds
import android.util.Log
import android.widget.LinearLayout
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.ismaeldivita.chipnavigation.ChipNavigationBar
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory


class Main : AppCompatActivity() {


    //var menu: ChipNavigationBar? = null
    //var fragmentManager: FragmentManager = supportFragmentManager
    //var fragmentTransaction: FragmentTransaction = fragmentManager.beginTransaction()

    lateinit var cropAdapter: CropAdapter
    val datas = mutableListOf<MainOutput>()

    var fragment = MainFragment()


    //뒤로가기
    //ImageView expandButton;
    var containerMain: LinearLayout? = null

    val changeBounds = ChangeBounds()


    override fun onCreate(savedInstanceState: Bundle?) {

        var transaction = supportFragmentManager.beginTransaction()

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)

        transaction.add(R.id.frame_layout, MainFragment())
        transaction.commit()
        var menu = findViewById(R.id.chipNavigationBar) as ChipNavigationBar
        //chipNavigationBar.setOnItemSelectedListener(this)
        Log.d(TAG, "call frame layout")



        //menu = findViewById(R.id.chipNavigationBar)
        //containerMain = findViewById(R.id.container_main)


        /*
        if (fragment == null) {
            fragmentManager = supportFragmentManager
            fragmentTransaction = fragmentManager.beginTransaction()
            fragmentTransaction.replace(R.id.frame_layout, MainFragment())
            fragmentTransaction.commit()
        }
        */


        //menu.setOnItemSelectedListener(object : ChipNavigationBar.OnItemSelectedListener() {
        menu.setOnItemSelectedListener(object : ChipNavigationBar.OnItemSelectedListener {
            //val transaction = supportFragmentManager.beginTransaction()
            override fun onItemSelected(i: Int) {
                when (i) {
                    R.id.home -> {
                        transaction = supportFragmentManager.beginTransaction()
                        Log.d(TAG, "call Home Fragment")
                        transaction.replace(R.id.frame_layout, MainFragment())
                        transaction.addToBackStack(null)
                        transaction.commit()
                    }
                        //fragment = MainFragment()
                    R.id.category -> {
                        transaction = supportFragmentManager.beginTransaction()
                        Log.d(TAG, "call Category Fragment")
                        transaction.replace(R.id.frame_layout, CategoryFragment())
                        transaction.addToBackStack(null)
                        transaction.commit()
                    }
                        //fragment = CategoryFragment()
                    R.id.search -> {
                        transaction = supportFragmentManager.beginTransaction()
                        Log.d(TAG, "call Search Fragment")
                        transaction.replace(R.id.frame_layout, SearchFragment())
                        transaction.addToBackStack(null)
                        transaction.commit()
                    }
                        //fragment = SearchFragment()
                    R.id.mypage -> {
                        transaction = supportFragmentManager.beginTransaction()
                        Log.d(TAG, "call MyPage Fragment")
                        transaction.replace(R.id.frame_layout, MyPageFragment())
                        transaction.addToBackStack(null)
                        transaction.commit()
                    }
                // fragment = MyPageFragment()
                }
                //fragmentManager = supportFragmentManager
                //fragmentTransaction = fragmentManager.beginTransaction()
                //fragmentTransaction.replace(R.id.frame_layout, fragment)
                //fragmentTransaction.commit()
            }
        })

        //recycler
        //initRecycler()

        //retrofit
        var retrofit = Retrofit.Builder()
            .baseUrl("https://cmsong111.pythonanywhere.com/") //해당 링크
            .addConverterFactory(GsonConverterFactory.create()) //Gson 사용 선언
            .build() //객체 생성

        //Django에 넣을 GET 발행 소스
        var MainService = retrofit.create(MainService::class.java)

        //통신 과정 소스 - 결과보여주기 위해 LoginOutput과 연결
        MainService.requestMain().enqueue(object : Callback<ArrayList<MainOutput>> {

        override fun onResponse(call: Call<ArrayList<MainOutput>>, response: Response<ArrayList<MainOutput>>) {

            //통신이 성공했을 때 - 응답값을 따옴

            var Main = response.body()

            if(Main != null){
                //val imageView: ImageView? = getView()?.findViewById(R.id.best_crop_1)

                //Glide.from(getActivity()).load(Main?.get(0)?.image).into(imageView)

                val result = Main?.get(0)?.fIDX + Main?.get(0)?.name + Main?.get(0)?.grade + Main?.get(0)?.weight + Main?.get(0)?.field + Main?.get(0)?.price + Main?.get(0)?.image + Main?.get(0)?.hitcount + Main?.get(0)?.kind + Main?.get(1)?.fIDX + Main?.get(1)?.name + Main?.get(1)?.grade + Main?.get(1)?.weight + Main?.get(1)?.field + Main?.get(1)?.price + Main?.get(1)?.image + Main?.get(1)?.hitcount + Main?.get(1)?.kind
                val duration = Toast.LENGTH_LONG

                //데이터 넘긱기
                intent.putExtra("DataList", result)

                //val applicationContext = getActivity()?.getApplicationContext()
                val toast = Toast.makeText(applicationContext, result, duration)
                toast.show()

                Log.d("retrofit", "res" + result)

            }else{
                Log.d("Error Code Test", response.errorBody()?.string()!!)
            }
        }

        override fun onFailure(call: Call<ArrayList<MainOutput>>, t: Throwable) {

            //통신이 실패했을 때
            Log.d("Debug", t.message.toString())

            //var dialog = AlertDialog.Builder(this@FRAGMENT_MAIN)
            //dialog.setTitle("통신실패")
            //dialog.setMessage("통신에 실패를 하였습니다.")
            //dialog.show()

            call.cancel()
        }
    })
    }

    /*
    private fun initRecycler() {
        cropAdapter = CropAdapter(this)
        today_crop_list.adapter = cropAdapter

        datas.apply{
            add(MainOutput(i))
            cropAdapter.datas = datas
            cropAdapter.notifyDataSetChanged()
        }

    }

     */
}