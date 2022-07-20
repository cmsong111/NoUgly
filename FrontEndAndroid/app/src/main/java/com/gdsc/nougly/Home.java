
package com.gdsc.nougly;


import android.os.Bundle;
import android.transition.ChangeBounds;
import android.util.Log;
import android.widget.LinearLayout;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.ismaeldivita.chipnavigation.ChipNavigationBar;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Home extends AppCompatActivity {
    /*
    ChipNavigationBar menu;
    FragmentManager fragmentManager;
    FragmentTransaction fragmentTransaction;
    Fragment fragment = null;
    //뒤로가기
    //ImageView expandButton;
    LinearLayout containerMain;

    ChangeBounds changeBounds = new ChangeBounds();

    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        //setContentView(R.layout.activity_home);

        menu = findViewById(R.id.chipNavigationBar);
        containerMain = findViewById(R.id.container_main);

        if(fragment == null){
            fragmentManager = getSupportFragmentManager();
            fragmentTransaction = fragmentManager.beginTransaction();
            fragmentTransaction.replace(R.id.frame_layout,new MainFragment());
            fragmentTransaction.commit();
        }

        menu.setOnItemSelectedListener(new ChipNavigationBar.OnItemSelectedListener() {
            @Override
            public void onItemSelected(int i) {
                switch (i){
                    case R.id.home:
                        fragment = new MainFragment();
                        break;
                    case R.id.category:
                        fragment = new CategoryFragment();
                        break;
                    case R.id.search:
                        fragment = new SearchFragment();
                        break;
                    case R.id.mypage:
                        fragment = new MyPageFragment();
                        break;
                }
                fragmentManager = getSupportFragmentManager();
                fragmentTransaction = fragmentManager.beginTransaction();
                fragmentTransaction.replace(R.id.frame_layout, fragment);
                fragmentTransaction.commit();
            }
        });


    }


    //retrofit
    Retrofit retrofit = new Retrofit.Builder()
            .baseUrl("https://cmsong111.pythonanywhere.com/") //해당 링크
            .addConverterFactory(GsonConverterFactory.create()) //Gson 사용 선언
            .build(); //객체 생성

    //Django에 넣을 GET 발행 소스
    MainService mainService = retrofit.create(MainService.class);

            //통신 과정 소스 - 결과보여주기 위해 LoginOutput과 연결
    mainService.getData("1").enqueue(new Callback<ArrayList<MainOutput>> () {
        @Override
        public void onResponse(@NonNull Call<ArrayList<MainOutput>> call, @NonNull Response<ArrayList<MainOutput>> response) {

            //통신이 성공했을 때 - 응답값을 따옴

            MainOutput Main = response.body();

            if(Main != null){
                val imageView: ImageView? = getView()?.findViewById(R.id.best_crop_1)

                Glide.from(getActivity()).load(Main?.get(0)?.image).into(imageView)

                val result = Main?.get(0)?.fIDX + Main?.get(0)?.name + Main?.get(0)?.grade + Main?.get(0)?.weight + Main?.get(0)?.field + Main?.get(0)?.price + Main?.get(0)?.image + Main?.get(0)?.hitcount + Main?.get(0)?.kind + Main?.get(1)?.fIDX + Main?.get(1)?.name + Main?.get(1)?.grade + Main?.get(1)?.weight + Main?.get(1)?.field + Main?.get(1)?.price + Main?.get(1)?.image + Main?.get(1)?.hitcount + Main?.get(1)?.kind
                val duration = Toast.LENGTH_LONG


                val applicationContext = getActivity()?.getApplicationContext()
                val toast = Toast.makeText(applicationContext, result, duration)
                toast.show();

                Log.d("retrofit", "res" + result);

            }else{
                Log.d("Error Code Test", response.errorBody()?.string()!!)
            }
        }

         public void onFailure(@NonNull Call<ArrayList<MainOutput>> call, @NonNull Throwable t) {

            //통신이 실패했을 때
            Log.d("Debug", t.message.toString())

            //var dialog = AlertDialog.Builder(this@FRAGMENT_MAIN)
            //dialog.setTitle("통신실패")
            //dialog.setMessage("통신에 실패를 하였습니다.")
            //dialog.show()

            call.cancel()
        }
    })
*/
    }
