package com.gdsc.nougly

import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST
import java.time.LocalDate
import java.util.*

interface RegisterService {
    @FormUrlEncoded
    @POST("/rest-auth/registration/")

    fun requestRegister(
        @Field("email") email: String?,
        @Field("password1") password: String?,
        @Field("password2") password2: String?,
        @Field("name") name: String?,
        @Field("phone_num") phoneNum: String?,
        @Field("date") date: String,
        @Field("gender") gender: String?,
        @Field("address") address: String?
    ): Call<RegisterOutput> //아웃풋을 정의하는 곳
}