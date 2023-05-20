package com.gdsc.nougly

//import com.bumptech.glide.Glide
//
//class CropAdapter(private val context: ArrayList<MainOutput>) : RecyclerView.Adapter<CropAdapter.ViewHolder>(){
////    var datas = mutableListOf<MainOutput>()
////    //ViewHolder에게 item을 보여줄 View로 쓰일 crop_recycler.xml 파일을 넘기면서 ViewHolder를 생성한다
//    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
////////        val view = LayoutInflater.from(context).inflate(R.layout.crop_recycler,parent,false)
////////        return ViewHolder(view)
//// }
////
//    override fun getItemCount(): Int = datas.size
////
////    //ViewHolder의 bind 메소드를 호출한다.
//    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
////        //TODO("Not yet implemented")
////        holder.bind(datas[position])
//    }
////
////    //inner class로 ViewHolder 정의
//    class ViewHolder(view: View) : RecyclerView.ViewHolder(view){
////        //이름 데이터와 이미지 데이터 가져오기
////        private val txtName : TextView = itemView.findViewById(R.id.cropName)
////        private val imgCrop : ImageView = itemView.findViewById(R.id.cropimage)
////
////        //frgment에 해당 데이터 집어넣기. onBindViewHolder의 역할을 대신한다.
//        fun bind(item: MainOutput){
////            txtName.text = item.name
////            Glide.with(itemView).load(item.image).into(imgCrop)
//        }
//    }
////
////
//}