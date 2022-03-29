package com.gdsc.nougly

import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST

interface LoginService {
    @FormUrlEncoded
    @POST("/rest-auth/login/")
    //여기가 인풋을 정의하는 곳
    fun requestLogin(
        @Field("email") email: String?,
        @Field("password") password: String?
    ): Call<LoginOutput> //아웃풋을 정의하는 곳
}

