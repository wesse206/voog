import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private createAuthHeader(): HttpHeaders {
    const username = 'voog';
    const password = 'HSDVoog2025';
    const auth = btoa(`${username}:${password}`);
    return new HttpHeaders({
      'Authorization': `Basic ${auth}`
    });
  }

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

  getTeacherlessLearners(TeacherCode: string, Day: number): Observable<any> {
    return this.http.get(`/api/getTeacherlessLearners?TeacherCode=${TeacherCode}&Day=${Day}`, { headers: this.createAuthHeader() })
  }

  getAbsentTeachers(): Observable<any> {
    return this.http.get(`/api/getAbsentTeachers`, { headers: this.createAuthHeader() })
  }

  setAbsentTeacher(TeacherCode: string, Day: number): Observable<any> {
    return this.http.get(`/api/setAbsentTeacher?TeacherCode=${TeacherCode}&Day=${Day}`, { headers: this.createAuthHeader() })
  }

  removeAbsentTeacher(TeacherCode: string, Day: number): Observable<any> {
    return this.http.get(`/api/removeAbsentTeacher?TeacherCode=${TeacherCode}&Day=${Day}`, { headers: this.createAuthHeader() })
  }

  getTeacherlessLearnersVoog(TeacherCode: string, Day: number): Observable<any> {
    return this.http.get(`/api/getTeacherlessLearnersVoog?TeacherCode=${TeacherCode}&Day=${Day}`, { headers: this.createAuthHeader() })
  }

  getTeacherlessLearnersBuddy(TeacherCode: string, Day: number): Observable<any> {
    return this.http.get(`/api/getTeacherlessLearnersBuddy?TeacherCode=${TeacherCode}&Day=${Day}`, { headers: this.createAuthHeader() })
  }

  getVoogTeachers(): Observable<any> {
    return this.http.get(`/api/getVoogTeachers`, { headers: this.createAuthHeader() })
  }

  constructor(private http: HttpClient) { }
}
