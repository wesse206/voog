import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  
  private TeacherCodeSource = new BehaviorSubject<string>('');
  TeacherCodeSource$ = this.TeacherCodeSource.asObservable();

  private TimeTableDaySource = new BehaviorSubject<number>(1);
  TimeTableDaySource$ = this.TimeTableDaySource.asObservable();

  TeacherCode(Code: string) {
    this.TeacherCodeSource.next(Code)
  }

  TimeTableDay(Day: number) {
    this.TimeTableDaySource.next(Day)
  }

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

  getTeacherlessLearnersBuddy(TeacherCode: string, Day:  number): Observable<any> {
    return this.http.get(`/api/getTeacherlessLearnersBuddy?TeacherCode=${TeacherCode}&Day=${Day}`)
  }

  getVoogTeachers(): Observable<any> {
    return this.http.get(`/api/getVoogTeachers`)
  }

  constructor(private http: HttpClient) { }
}
