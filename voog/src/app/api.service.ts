import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  getTeacherlessLearners(TeacherCode: string, Day:  number): Observable<any> {
    return this.http.get(`/api/getTeacherlessLearners?TeacherCode=${TeacherCode}&Day=${Day}`)
  }

  getAbsentTeachers(): Observable<any> {
    return this.http.get(`/api/getAbsentTeachers`)
  }

  setAbsentTeacher(TeacherCode: string, Day:  number): Observable<any> {
    return this.http.get(`/api/setAbsentTeacher?TeacherCode=${TeacherCode}&Day=${Day}`)
  }

  removeAbsentTeacher(TeacherCode: string, Day:  number): Observable<any> {
    return this.http.get(`/api/removeAbsentTeacher?TeacherCode=${TeacherCode}&Day=${Day}`)
  }

  getTeacherlessLearnersVoog(TeacherCode: string, Day:  number): Observable<any> {
    return this.http.get(`/api/getTeacherlessLearnersVoog?TeacherCode=${TeacherCode}&Day=${Day}`)
  }

  constructor(private http: HttpClient) { }
}
